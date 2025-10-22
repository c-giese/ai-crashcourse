# Network Requests TODO by Fred

Erklären, wie requests ablaufen, am besten an der Tafel mit ollama als Beispiel

Dann auf das Requests Modul von python eingehen und das untenstehende simple beispiel in einer einfach python datei ausführen

https://www.w3schools.com/python/module_requests.asp

## Basic Example

```
import requests

url = 'https://www.w3schools.com/python/demopage.php'
myobj = {'somekey': 'somevalue'}

x = requests.post(url, json = myobj)

#print the response text (the content of the requested file):

print(x.text)
```
