import pandas as pd
import pickle
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}



# Slim version = version allégée de Python 
# FROM python:3.10.6-slim 

# # Install requirements 
# COPY requirements.txt requirements.txt 
# RUN pip install --no-cache-dir --upgrade pip 
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy our code 
# COPY Landing.page Landing.page
# COPY api api
# COPY models models

# COPY credentials.json credentials.json

# CMD uvicorn api.fast:app --host 0.0.0.0 --port $PORT