from fastapi import APIRouter

from app.services.run_history_service import get_all

router = APIRouter()

@router.get("")
def get_history():
    return get_all()