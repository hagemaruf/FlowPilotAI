from fastapi import APIRouter

from app.services.template_service import get_all

router = APIRouter()

@router.get("")
def get_templates():

    return get_all()