from pydantic import BaseModel
from datetime import datetime
from uuid import uuid4

class Workflow(BaseModel):
    id: str
    name: str
    description: str
    prompt: str 
    created_at: datetime