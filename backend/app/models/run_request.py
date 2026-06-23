from pydantic import BaseModel

class RunWorkflowRequest(BaseModel):
    workflow_id: str
    user_input: str