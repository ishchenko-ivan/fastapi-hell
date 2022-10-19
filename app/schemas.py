from datetime import datetime
from pydantic import BaseModel
from typing import Optional
from fastapi import Body

class Item(BaseModel):
    title: str
    price: float
    quantity: int
    upd_date: datetime


class UpdateItem(BaseModel):
    title: Optional[str] = None
    price: Optional[float] = None
    quantity: Optional[int] = None
    upd_date: Optional[datetime] = None