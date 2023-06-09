from typing import Optional 
from pydantic import BaseModel
from datetime import date, datetime 


class JobBase(BaseModel):
    title : Optional[str] = None 
    company : Optional[str] = None 
    company_url : Optional[str] = None 
    location : Optional[str] = "Remote"
    description : Optional[str] = None 
    date_posted : Optional[date] = datetime.now().date() 

class CreateJob(JobBase):
    title : str 
    company: str 
    location: str 
    description: str 

class UpdateJob(JobBase):
    title : str 
    company: str 
    location: str 
    description: str 

class ShowJob(JobBase):
    title : str 
    company : str 
    company_url : Optional[str]
    location : str 
    date_posted : date 
    description : Optional[str] 

    ## lets convert non dict obj to json
    class Config():
        orm_mode = True


