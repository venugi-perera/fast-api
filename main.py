from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import numpy as np
import pickle
import os
from pydantic import BaseModel
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust as needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model_path = 'model'
model_file = os.path.join(model_path, 'model.pkl')

if not os.path.exists(model_file):
    logger.error(f"Model file not found at {model_file}")
    raise FileNotFoundError(f"Model file not found at {model_file}")

with open(model_file, 'rb') as f:
    model = pickle.load(f)
    logger.info("Model loaded successfully")

class PredictCaloriesItem(BaseModel):
    RPC_RATE: int 
    KEPT_RATE: int
    MONTH_END_DPD: int

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post('/predict')
async def predict_calories(item: PredictCaloriesItem):
    try:
        df = pd.DataFrame([item.dict()])
        logger.info(f"Input data: {df}")
        preds = model.predict(df)
        rounded_preds = np.round(preds)
        logger.info(f"Prediction: {rounded_preds}")
        return {'prediction': int(rounded_preds[0])}
    except Exception as e:
        logger.error(f"Prediction error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
