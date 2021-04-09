import requests

url="http://127.0.0.1:5000/"

response =requests.put(url + "video/1", {"likes":10, "name":"Shishank", "views": 100000})
print (response.json())
input()

response =requests.get(url + "video/1")
print (response.json())