from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def health_check():
    return "the health check is successful!"