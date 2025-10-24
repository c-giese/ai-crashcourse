import requests
import json

url = "http://localhost:11434/api/chat"
payload = {
  "model": "gemma3:1b",
  "messages": [
    {
      "role": "user",
      "content": "hi"
    }
  ],
  "stream": True
}

# 1. Intuitiver ansatz mit Stream
response = requests.post(url, json=payload)
if response.status_code == 200:
    for line in  response.iter_lines():
        if line: 
            print(line)
else:
    print(f"Error: {response.status_code}")