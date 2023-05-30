## Job Board App
- This project is about creating a job board wesite with the following functionalities:
    - List a job
    - Details of the Job post
    - Create a job post
    - Update the job
    - Delete the job
    - Permissions (Authorization required, only superuser and the original authe can delete)
    - Authentication (Registration and Login)
    - Test our Endpoint
    - Test Coverage
    - Webapp for Jobboard

## Technology Stack
<img src="tech_stack.jpg" alt="Alt text" title="Optional title">


## Environment Configuration
- Setting up project Env using the following:
    - pip install pipenv 
    - pipenv install fastapi uvicorn
- Create a simple Fastapi app
    - mkdir app 
    - touch app/main.py
- Running the app 
    - uvicorn app.main:app --reload

- Create a Dockerfile to run the app
    - Dockerfile
    - Build the docker image 
        - docker build . 
- Create the docker-compose file to run 
    - Build the docker-compose file
        - To run fastapi app, postgres, pgadmin
        - docker-compose build
        - docker-compuse up
   
