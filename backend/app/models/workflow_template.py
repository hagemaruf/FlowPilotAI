from typing import List
from pydantic import BaseModel
from app.models.workflow_step import WorkflowStep

class WorkflowTemplate(BaseModel):
    name: str
    description: str
    steps: List[WorkflowStep]