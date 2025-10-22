import requests

url = "https://jsonplaceholder.typicode.com/posts"
payload = {"userId": 1, "title": "Hallo", "body": "Test"}

response = requests.post(url, json=payload)
print(response.text)