import requests

url = "http://localhost:11434/api/chat"
payload = {
  "model": "gemma3:1b",
  "messages": [
    {
      "role": "user",
      "content": "hi"
    }
  ],
  "stream": False
}

# Sends the request to the chatbot API and stores the response
response = requests.post(url, json=payload)
# Prints the content of the chatbot's reply if the request was successful
if response.status_code == 200: # status code 200 means OK
    response_data = response.json()
    print(response_data['message']['content'])
else:
    print(f"Error: {response.status_code}")