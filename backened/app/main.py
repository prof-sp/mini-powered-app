from fastapi import FastAPI, UploadFile, File, Depends, BackgroundTasks
from fastapi.responses import JSONResponse
import shutil, os, uuid
from sqlalchemy.orm import Session
from . import database, crud, ml_inference, models
from .schemas import InspectionOut, InspectionCreate

app = FastAPI(title="AI Food Quality Monitoring")

# create DB tables (for demo; production: use migrations)
models.Base.metadata.create_all(bind=database.engine)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

UPLOAD_DIR = os.getenv("UPLOAD_DIR", "/tmp/uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/inspect", response_model=InspectionOut)
async def inspect(file: UploadFile = File(...), payload: InspectionCreate = None, db: Session = Depends(get_db), background_tasks: BackgroundTasks = None):
    # save file
    ext = os.path.splitext(file.filename)[1]
    filename = f"{uuid.uuid4().hex}{ext}"
    filepath = os.path.join(UPLOAD_DIR, filename)
    with open(filepath, "wb") as f:
        shutil.copyfileobj(file.file, f)

    # run inference (fast synchronous call — adapt to background if heavy)
    with open(filepath, "rb") as f:
        result = ml_inference.predict(f)

    ins = crud.create_inspection(db, image_path=filepath, label=result["label"], confidence=result["confidence"], batch_id=(payload.batch_id if payload else None), notes=(payload.notes if payload else None))
    return ins

@app.get("/inspections")
def list_inspections(db: Session = Depends(get_db), limit: int = 50):
    items = db.query(models.Inspection).order_by(models.Inspection.created_at.desc()).limit(limit).all()
    return items
