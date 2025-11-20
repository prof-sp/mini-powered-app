from sqlalchemy import Column, Integer, String, DateTime, Float, Text
from sqlalchemy.sql import func
from .database import Base

class Batch(Base):
    __tablename__ = "batches"
    id = Column(Integer, primary_key=True, index=True)
    batch_code = Column(String, index=True)
    origin = Column(String, nullable=True)
    product_type = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Inspection(Base):
    __tablename__ = "inspections"
    id = Column(Integer, primary_key=True, index=True)
    batch_id = Column(Integer, index=True)
    image_path = Column(String)
    label = Column(String, index=True)  # Fresh / Spoiled / Contaminated
    confidence = Column(Float)
    severity = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    notes = Column(Text, nullable=True)
