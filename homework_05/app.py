"""
Домашнее задание №5
Первое веб-приложение

создайте базовое приложение на Flask
создайте index view /
добавьте страницу /about/, добавьте туда текст
создайте базовый шаблон (используйте https://getbootstrap.com/docs/5.0/getting-started/introduction/#starter-template)
в базовый шаблон подключите статику Bootstrap 5 и добавьте стили, примените их
в базовый шаблон добавьте навигационную панель nav (https://getbootstrap.com/docs/5.0/components/navbar/)
в навигационную панель добавьте ссылки на главную страницу / и на страницу /about/ при помощи url_for
"""
import datetime
from datetime import date
from fastapi import FastAPI, Request, APIRouter
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
import uvicorn
from model.event import Event

app = FastAPI()
templates = Jinja2Templates("templates")
event_router = APIRouter(prefix="/event")


def _create_default_events():
    eventlist = []
    for i in range(4):
        item_data = {
            "event_id": i+1,
            "event_description": "Some description " + str(i+1),
            "event_date": datetime.date.today() + datetime.timedelta(days=i),
            "event_pic": 'https://masterpiecer-images.s3.yandex.net/34e974e177bb11ee9ad5ceda526c50ab:upscaled',
            "event_title": "title" + str(i+1)
        }
        eventlist.append(Event(**item_data))
    return eventlist


events = _create_default_events()


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    eventlist = events
    return templates.TemplateResponse("index.html", {"request": request, "events": eventlist})


@app.get("/about/", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})


@event_router.get("/list/", response_class=HTMLResponse)
async def list(request: Request):
    return templates.TemplateResponse("events.html", {"request": request, "events": events})


@event_router.get("/add", response_class=HTMLResponse)
async def add_event_get(request: Request):
    return templates.TemplateResponse("add_event.html", {"request": request, "events": events})


@event_router.post('/add', response_class=HTMLResponse)
async def add_event_post():
    return RedirectResponse(url=event_router.url_path_for("add_event_get"), status_code=303)


@event_router.get("/delete/", response_class=HTMLResponse)
async def delete_event_get(request: Request):
    return templates.TemplateResponse("delete_event.html", {"request": request, "events": events})


@event_router.post("/delete/", response_class=HTMLResponse)
async def delete_event_post(request: Request):
    return RedirectResponse(url=event_router.url_path_for("delete_event_get"), status_code=303)

@event_router.get("/change_event/", response_class=HTMLResponse)
async def change(request: Request):
    return templates.TemplateResponse("change_event.html", {"request": request, "events": events})


app.include_router(event_router)

if __name__=="__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000)



