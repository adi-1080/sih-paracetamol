from fastapi import APIRouter, UploadFile, File
from src.controllers.model import main_model_controller

router = APIRouter()

@router.post("/main-model")
async def main_model(file: UploadFile = File(...)):
    return await main_model_controller(file)