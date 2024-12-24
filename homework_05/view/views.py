from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import FastAPI, Request, APIRouter

router = APIRouter()
templates = Jinja2Templates("templates")


@router.get("/", response_class=HTMLResponse, summary="Main page summary", description="Main page description")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@router.get("/about/", response_class=HTMLResponse, summary="About page summary", description="About page description")
async def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})
