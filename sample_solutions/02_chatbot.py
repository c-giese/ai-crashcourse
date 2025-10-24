import json

import requests

url = "http://localhost:11434/api/chat"
payload = {
    "model": "gemma3:1b",
    "messages": [{"role": "user", "content": "hi"}],
    "stream": True,
}

response = requests.post(url, json=payload, stream=True)

if response.status_code == 200:
    # Print each chunk as it arrives, simulating typing
    for line in response.iter_lines(decode_unicode=True):
        if line:
            # unpack the bytes (the format in which the lines arrive)
            data = json.loads(line)
            chunk = data["message"]["content"]
            print(chunk, end="", flush=True)
    print()  # Newline after completion
else:
    print(f"Error: {response.status_code}")
