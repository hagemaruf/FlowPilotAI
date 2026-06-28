from fastapi import APIRouter, HTTPException

from uuid import uuid4
from datetime import datetime

from app.models.run_request import RunWorkflowRequest
from app.models.run_history import RunHistory

from app.services.run_history_service import add
from app.services.workflow_service import get_by_id
from app.services.workflow_engine import execute

router = APIRouter()


@router.post("")
def run_workflow(
    request: RunWorkflowRequest
):

    workflow = get_by_id(
        request.workflow_id
    )

    if workflow is None:

        raise HTTPException(
            status_code=404,
            detail="Workflow not found"
        )

    execution_result = execute(
        workflow,
        request.user_input
    )

    history = RunHistory(
        id=str(uuid4()),
        workflow_name=workflow.name,
        user_input=request.user_input,
        result=execution_result["final_result"],
        executed_at=datetime.utcnow()
    )

    add(history)

    return execution_result