from fastapi import FastAPI
from routers import plan,dashboard
import uvicorn



app = FastAPI()

app.include_router(plan.router, prefix="" , tags=["plan"])

@app.get("/")
def root():
    return {"message": "Fitness Agentic AI Backend is running"}



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)