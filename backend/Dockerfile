FROM python:3.12-alpine

## Set the working directory
WORKDIR /code 

# Install necessary system dependencies
RUN apk add --no-cache gcc musl-dev libffi-dev

COPY requirements.txt ./ 

RUN pip install --no-cache-dir -r requirements.txt 

COPY . . 


ENTRYPOINT [ "uvicorn" ]

CMD ["app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]