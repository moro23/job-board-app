from multiprocessing import synchronize
from sqlalchemy.orm import Session 

from schemas.jobs import CreateJob 
from db.models.jobs import Job 

## function for creating a job
def create_new_job(job:CreateJob, db: Session, owner_id: int):
    job_object = Job(**job.dict(), owner_id=owner_id)
    db.add(job_object)
    db.commit() 
    db.refresh(job_object)
    return job_object 

## function for retrieving a job
def retreive_job(id:int, db:Session):
    item = db.query(Job).filter(Job.id == id).first() 
    return item 

## function for listing all jobs
def list_jobs(db: Session):
    jobs = db.query(Job).all().filter(Job.is_active == True)
    return jobs

## 
def update_job_by_id(id:int, job: CreateJob, db: Session, owner_id):
    existing_job = db.query(Job).filter(Job.id == id) 
    if not existing_job:
        return 0
    Job.__dict__.update(owner_id==owner_id)
    existing_job.update(job.__dict__)
    db.commit()
    return 1

def delete_job_by_id(id:int, job: CreateJob, db: Session, owner_id):
    existing_job = db.query(Job).filter(Job.id == id)
    if not existing_job:
        return 0
    existing_job.delete(synchronize_session=False)
    db.commit() 
    return 1
    