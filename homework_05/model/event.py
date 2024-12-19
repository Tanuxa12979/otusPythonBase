from pydantic import BaseModel
from datetime import date

class Event(BaseModel):
    event_id: int
    event_title: str
    event_date: date
    event_pic: str
    event_description: str