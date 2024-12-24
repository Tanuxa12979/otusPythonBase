from pydantic import BaseModel
from datetime import date


class Event(BaseModel):
    id: int
    title: str
    event_date: date
    pic: str
    description: str
