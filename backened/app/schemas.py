from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class InspectionCreate(BaseModel):
    batch_id: Optional[int]
    notes: Optional[str]

class InspectionOut(BaseModel):
    id: int
    batch_id: Optional[int]
    image_path: str
    label: str
    confidence: float
    created_at: datetime

    class Config:
        orm_mode = True
