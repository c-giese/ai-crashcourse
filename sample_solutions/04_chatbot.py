import json

import requests

# Greeting message
print("Hi how can i help you today? To stop the chat, type /bye")

while True:
    # Prompt the user and check if they want to stop the chat.
    user_query = input("You: ")
    if user_query.lower() == "/bye":
        print("Assistant: Goodbye!")
        break

    url = "http://localhost:11434/api/chat"
    payload = {
        "model": "phi3:latest",
        "messages": [{"role": "user", "content": user_query}],
        "stream": True,
    }
    response = requests.post(url, json=payload, stream=True)
    if response.status_code == 200:
        print(
            "Assistant: ", end="", flush=True
        )  # Add an indicator that this is the assistant's message
        # Print each chunk as it arrives, simulating typing
        for line in response.iter_lines(decode_unicode=True):
            if line:
                data = json.loads(line)
                chunk = data["message"]["content"]
                print(chunk, end="", flush=True)
        print()  # Newline after completion
    else:
        print(f"Error: {response.status_code}")
