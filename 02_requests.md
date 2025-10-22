# Network Requests

Try the following requests with python to get familiar with GET and POST:

## Basic Examples

GET:

```
import requests

x = requests.get('https://w3schools.com/python/demopage.htm')

print(x.text)
```

POST:

```
import requests

url = "https://jsonplaceholder.typicode.com/posts"
payload = {"userId": 1, "title": "Hallo", "body": "Test"}

response = requests.post(url, json=payload)
print(response.json())
```
