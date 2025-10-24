import json

import requests

# Send a Greeting message and prompt the user to send a message.
user_query = input("Hi, how can i help you today?\n")


url = "http://localhost:11434/api/chat"
payload = {
    "model": "phi3:latest",
    "messages": [{"role": "user", "content": user_query}],
    "stream": True,
}
response = requests.post(url, json=payload, stream=True)
if response.status_code == 200:
    # Print each chunk as it arrives, simulating typing
    for line in response.iter_lines(decode_unicode=True):
        if line:
            data = json.loads(line)
            chunk = data["message"]["content"]
            print(chunk, end="", flush=True)
    print()  # Newline after completion
else:
    print(f"Error: {response.status_code}")
