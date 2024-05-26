from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import pickle
import os 
import pandas as pd
import numpy as np
from models.user import Todo
from config.database import collection_name, risk_collection
from schema.schemas import list_serial
from schema.risk import risk_serial
from fastapi.middleware.cors import CORSMiddleware

router = APIRouter()

model_path = 'model'

class PredictCaloriesItem(BaseModel):
    RPC_RATE: int 
    KEPT_RATE: int
    MONTH_END_DPD: int

with open(os.path.join(model_path, 'model.pkl'), 'rb') as f:
    model = pickle.load(f)

@router.get("/")
def read_root():
    return {"Hello": "World"}

@router.post('/predict')
async def predict_calories(item: PredictCaloriesItem):
    df = pd.DataFrame([item.dict()])
    preds = model.predict(df)
    rounded_preds = np.round(preds)
    return {'prediction': int(rounded_preds)}

@router.get("/index", response_class=HTMLResponse)
async def get_index(request: Request):
    with open("index.html", "r") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)

@router.get('/test')
async def get_todos():
    query = {"YEAR": 2024, "MONTH": "JANUARY"}

    todos = list_serial(collection_name.find(query))
    return todos

@router.get('/risk')
async def get_risk():
    todos = list_serial(risk_collection.find())
    return todos
