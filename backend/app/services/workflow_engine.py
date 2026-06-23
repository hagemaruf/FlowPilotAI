from app.agents.ollama_agent import run as run_agent


def execute(prompt: str, user_input: str):

    final_prompt = f"""
{prompt}

Input:

{user_input}
"""

    return run_agent(final_prompt)