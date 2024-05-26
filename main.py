from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from routes.route import router

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

# @router.post('/predict')
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
