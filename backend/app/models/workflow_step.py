from pydantic import BaseModel

class WorkflowStep(BaseModel):
    order: int
    name: str
    prompt: str