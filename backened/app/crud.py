from sqlalchemy.orm import Session
from . import models, schemas

def create_inspection(db: Session, *, image_path: str, label: str, confidence: float, batch_id: int=None, notes: str=None):
    ins = models.Inspection(batch_id=batch_id, image_path=image_path, label=label, confidence=confidence, notes=notes)
    db.add(ins)
    db.commit()
    db.refresh(ins)
    return ins
