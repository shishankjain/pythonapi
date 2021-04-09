import requests

url="http://127.0.0.1:5000/"

data = [{"likes": 78, "name": "Joe", "views": 100000},
{"likes": 78, "name": "How to make an api", "views": 100999},
{"likes": 7800000000, "name": "SHISHANK JAIN", "views": 100000}]

for i in range (len(data)):
  response= requests.put(url + "video/" + str(i), data[i])
  print (response.json())

input()
response =requests.get(url + "video/6")
print (response.json())