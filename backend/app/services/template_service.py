from app.models.workflow_template import WorkflowTemplate
from app.models.workflow_step import WorkflowStep

templates = [

    WorkflowTemplate(
        name="Meeting Notes Processor",
        description="Extract action items from meeting notes",
        steps=[
            WorkflowStep(
                order=1,
                name="Extract Action Items",
                prompt="""
Extract all action items from the meeting notes.
Return as a bullet list.
"""
            ),
            WorkflowStep(
                order=2,
                name="Assign Owners",
                prompt="""
For every action item identify the owner.
"""
            ),
            WorkflowStep(
                order=3,
                name="Generate Summary",
                prompt="""
Generate an executive summary.
"""
            )
        ]
    ),

    WorkflowTemplate(
        name="LinkedIn Post Generator",
        description="Generate professional LinkedIn posts",
        steps=[
            WorkflowStep(
                order=1,
                name="Summarize Project",
                prompt="""
Summarize the project update.
"""
            ),
            WorkflowStep(
                order=2,
                name="Write LinkedIn Post",
                prompt="""
Create a professional LinkedIn post.
"""
            ),
            WorkflowStep(
                order=3,
                name="Generate Hashtags",
                prompt="""
Generate relevant hashtags.
"""
            )
        ]
    ),

    WorkflowTemplate(
        name="Customer Support Agent",
        description="Analyze support tickets",
        steps=[
            WorkflowStep(
                order=1,
                name="Classify Ticket",
                prompt="""
Classify the customer ticket.
"""
            ),
            WorkflowStep(
                order=2,
                name="Determine Priority",
                prompt="""
Determine ticket priority.
"""
            ),
            WorkflowStep(
                order=3,
                name="Generate Response",
                prompt="""
Generate a professional response.
"""
            )
        ]
    )

]


def get_all():
    return templates