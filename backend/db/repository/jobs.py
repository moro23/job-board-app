from sqlalchemy.orm import Session 

from schemas.jobs import CreateJob 
from db.models.jobs import Job 

def create_new_job(job:CreateJob, db: Session, owner_id: int):
    job_object = Job(**job.dict(), owner_id=owner_id)
    db.add(job_object)
    db.commit() 
    db.refresh(job_object)
    return job_object