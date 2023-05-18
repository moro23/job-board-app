from turtle import title
## lets import our project libraries
from fastapi import FastAPI
from core.config import settings

## lets create an instance of our fastapi app 
## lets also init with the project title and version
app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)

## lets create a decorator with an endpoint
@app.get("/")

## lets create a function to display a simple message
def hello_api():
    return {"msg": "Hello API"}