from fastapi import APIRouter, HTTPException

from app.models.run_request import RunWorkflowRequest

from app.services.workflow_service import get_by_id
from app.services.workflow_engine import execute

router = APIRouter()


@router.post("")
def run_workflow(request: RunWorkflowRequest):

    workflow = get_by_id(
        request.workflow_id
    )

    if workflow is None:

        raise HTTPException(
            status_code=404,
            detail="Workflow not found"
        )

    result = execute(
        workflow.prompt,
        request.user_input
    )

    return {
        "result": result
    }