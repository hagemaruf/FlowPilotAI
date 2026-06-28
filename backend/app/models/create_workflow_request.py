from pydantic import BaseModel
from typing import List

from app.models.workflow_step import WorkflowStep


class CreateWorkflowRequest(BaseModel):

    name: str
    description: str
    steps: List[WorkflowStep]