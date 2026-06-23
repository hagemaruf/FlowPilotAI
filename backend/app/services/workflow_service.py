from datetime import datetime
from app.models.workflow import Workflow
from uuid import uuid4

workflows = []

def get_all():
    return workflows

def create(name: str, description: str, prompt: str):
    workflow = Workflow(
        id=str(uuid4()),
        name=name,
        description=description,
        prompt=prompt,
        created_at=datetime.utcnow()
    )

    workflows.append(workflow)

    return workflow

def delete(workflow_id: str):
    global workflows

    workflows = [
        w for w in workflows
        if w.id != workflow_id
    ]

def get_by_id(workflow_id: str):

    for workflow in workflows:

        if workflow.id == workflow_id:
            return workflow

    return None