from pydantic import BaseModel
from datetime import datetime
from uuid import uuid4
from typing import List

from app.models.workflow_step import WorkflowStep

class Workflow(BaseModel):
    id: str
    name: str
    description: str
    steps: List[WorkflowStep]
    created_at: datetime