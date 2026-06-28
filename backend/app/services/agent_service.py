import ollama

def execute_step(
    prompt: str,
    user_input: str
):

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content":
                    f"{prompt}\n\n{user_input}"
            }
        ]
    )

    return response["message"]["content"]