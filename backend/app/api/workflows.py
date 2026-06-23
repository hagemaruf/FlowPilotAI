from fastapi import APIRouter
from pydantic import BaseModel

from app.services import workflow_service

router = APIRouter()

class CreateWorkflowRequest(BaseModel):
    name: str
    description: str
    prompt: str

@router.get("")
def get_workflows():
    return workflow_service.get_all()

@router.post("")
def create_workflow(request: CreateWorkflowRequest):
    return workflow_service.create(
        request.name,
        request.description,
        request.prompt
    )

@router.delete("/{workflow_id}")
def delete_workflow(workflow_id: str):
    workflow_service.delete(workflow_id)

    return {
        "success": True
    }