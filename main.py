import requests

payload = {"name": "Sam"}
response = requests.get("https://playground.learnqa.ru/api/hello", params=payload)
print(response.text