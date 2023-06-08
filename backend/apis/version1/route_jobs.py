from fastapi import APIRouter 
from sqlalchemy.orm import Session 
from fastapi import Depends, HTTPException, status

from db.session import get_db
from db.models.jobs import Job
from schemas.jobs import CreateJob, ShowJob
from db.repository.jobs import create_new_job, retreive_job

router = APIRouter()

## lets add a function for getting job data sending it to model
@router.post("/create-job/", response_model=ShowJob)
def create_job( job:CreateJob, db: Session = Depends(get_db)):
    current_user = 1
    job = create_new_job(job=job, db=db, owner_id=current_user)
    return job

## lets add a function for fetching data of a job with a given id
@router.get("/get/{id}", response_model=ShowJob)
def read_job(id:int, db:Session = Depends(get_db)):
    job = retreive_job(id=id, db=db)
    if not job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Job with this id {id} does not exist")
    return job 