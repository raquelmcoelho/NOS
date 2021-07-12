import requests

p = {"gato": 666}
cat1 = requests.get("https://httpbin.org/get", params=p)
print(cat1.text)
cat = requests.post("https://httpbin.org/post", data=p)
print(cat.text)