from datetime import date
from typing import List

from fastapi.routing import APIRouter
from fastapi import FastAPI, Request, HTTPException
from homework_05.model.event_storage import EventStorage

event_router = APIRouter()


@event_router.get("/event/list/")
async def event_list():
    return EventStorage.show_events()


@event_router.post("/event/add/")
async def add_event(title: str, event_date: date, pic: str, description: str):
    try:
        event = EventStorage.add_event(title, event_date, pic, description)
        return f'Event {event} was added successfully'
    except:
        return HTTPException(400, "Event not valid")


@event_router.get("/event/{id}/")
async def change(id: str):
    event = EventStorage.show_event(id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event
