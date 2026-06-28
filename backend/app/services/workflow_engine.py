from app.services.agent_service import execute_step


def execute(workflow, user_input: str):

    current_input = user_input

    step_results = []

    for step in sorted(workflow.steps, key=lambda s: s.order):

        result = execute_step(
            step.prompt,
            current_input
        )

        step_results.append({
            "step": step.name,
            "result": result
        })

    return {
        "final_result": current_input,
        "steps": step_results
    }