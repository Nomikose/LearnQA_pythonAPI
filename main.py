import requests

payload = {"name": "Nik"}
response = requests.get("https://playground.learnqa.ru/api/hello", params=payload)
print(response.text)