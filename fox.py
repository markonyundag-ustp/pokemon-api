import requests

response = requests.get("http://randomfox.ca/floof")
# print(response.status_code)
# print(response.text)
# print(response.json())


fox = response.json()
print(fox['image'])
