from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
def index():
    return {"Hello":{"World":"HI"}}

@app.get('/about') 
def about():
    return {'deta':'about page'}
 