#route_general_pages.py

## lets import all modules
from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

## lets create an object of Jinja2Templates
## and instantiate it with director name
templates = Jinja2Templates(directory="templates")

## lets create an instance of APIRouter
general_pages_router = APIRouter()


@general_pages_router.get("/")
async def home(request: Request):
    return templates.TemplateResponse("general_pages/homepage.html", {"request": request})