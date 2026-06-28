from pydantic import BaseModel
from datetime import datetime

class RunHistory(BaseModel):
    id: str
    workflow_name: str
    user_input: str
    result: str
    executed_at: datetime