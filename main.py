from fastapi import FastAPI
from src.routers import home, health_check, main_model, mobile_model
import uvicorn

app = FastAPI()

app.include_router(home.router)
app.include_router(health_check.router)
app.include_router(main_model.router)
app.include_router(mobile_model.router)


def main():
    print("Hello from ml-backend!")
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)  

if __name__ == "__main__":
    main()
