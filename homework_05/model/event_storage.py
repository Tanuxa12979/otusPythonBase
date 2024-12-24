from pydantic import ValidationError
from typing import List, Optional
from homework_05.model.event import Event
from datetime import date
from homework_05.model.csv_work import CSVWork


class EventStorage:

    @staticmethod
    def _next_id(events: List[Event]) -> int:
        "Генерация нового айди при добавлении записи"
        return max([int(event["id"]) for event in events])

    @staticmethod
    def add_event(title: str, event_date: date, pic: str, description: str) -> Event:
        "Создание и добавление нового события"
        events = CSVWork.read_csv()
        id_event = int(EventStorage._next_id(events))+1
        try:
            new_event = Event(id=id_event, title=title, event_date=event_date, pic=pic, description=description)
            CSVWork.add_csv(new_event.model_dump())
            return new_event
        except ValidationError as er:
            return {"error": er.text()}

    @staticmethod
    def show_events() -> List[Event]:
        "Получение событий из файла"
        events = CSVWork.read_csv()
        return events

    @staticmethod
    def show_event(id_event: int) -> Optional[Event]:
        "Получение события из файла и возврат события найденного по айди"
        events = CSVWork.read_csv()
        for event in events:
            if event["id"] == id_event:
                return event



