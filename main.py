from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import numpy as np
import pickle
import os 
from pydantic import BaseModel

# from routes.route import router

app = FastAPI()

model_path = 'model'

class PredictCaloriesItem(BaseModel):
    RPC_RATE: int 
    KEPT_RATE: int
    MONTH_END_DPD: int

with open(os.path.join(model_path, 'model.pkl'), 'rb') as f:
    model = pickle.load(f)

@app.get("/")
def read_root():
    return {"Hello": "World"}

# @app.post('/predict')
# async def predict_calories(item: PredictCaloriesItem):
#     df = pd.DataFrame([item.dict()])
#     preds = model.predict(df)
#     rounded_preds = np.round(preds)
#     return {'prediction': int(rounded_preds)}

# origins = [
#     "http://localhost:3000",
#     "http://localhost:8000",
#     "https://vertexfinance.vercel.app",
#     "https://webrouter.vercel.app"
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins= ["*"],
#     allow_credentials=True,
#     allow_methods=["GET", "POST", "PUT", "DELETE"],
#     allow_headers=["*"],
# )

# app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
