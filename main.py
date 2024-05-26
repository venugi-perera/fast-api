from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import numpy as np
import pickle
import os
from pydantic import BaseModel

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
    raise FileNotFoundError(f"Model file not found at {model_file}")

with open(model_file, 'rb') as f:
    model = pickle.load(f)

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
        preds = model.predict(df)
        rounded_preds = np.round(preds)
        return {'prediction': int(rounded_preds[0])}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
