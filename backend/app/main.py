## lets import our project libraries
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from core.config import settings
#from apis.general_pages.route_homepage import general_pages_router
from apis.base import api_router
from db.session import engine 
from db.base import Base


def include_router(app):
    app.include_router(api_router)

# ## lets specify the dir to keep all static files
# def configure_static(app):
#     app.mount("/static", StaticFiles(directory="static"), name="static")

## lets create our tables 
def create_tables():
    Base.metadata.create_all(bind=engine)


def start_application():
    ## lets create an instance of our fastapi app 
    ## lets also init with the project title and version
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    include_router(app)
    # configure_static(app)
    create_tables()
    return app

app = start_application()


