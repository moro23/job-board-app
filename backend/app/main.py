## lets import our project libraries
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from core.config import settings
from apis.general_pages.route_homepage import general_pages_router

def include_router(app):
    app.include_router(general_pages_router)

## lets specify the dir to keep all static files
def configure_static(app):
    app.mount("/static", StaticFiles(directory="static"), name="static")

def start_application():
    ## lets create an instance of our fastapi app 
    ## lets also init with the project title and version
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    include_router(app)
    configure_static(app)
    return app

app = start_application()


