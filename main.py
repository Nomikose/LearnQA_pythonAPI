from json.decoder import JSONDecodeError
import requests

# payload = {"name": "User"}
# response = requests.get("https://playground.learnqa.ru/api/hello", params=payload)
# print(response.text)

# response = requests.get("https://playground.learnqa.ru/api/hello", params={"name": "User"})
# parsed_response_text = response.json()
# print(parsed_response_text["answer"])

# response = requests.get("https://playground.learnqa.ru/api/get_text")
# print(response.text)

# try:
#     parsed_response_text = response.json()
#     print(parsed_response_text)
# except JSONDecodeError:
#     print("Response is not a JSON format")

response = requests.post("https://playground.learnqa.ru/api/check_type", data={"param1": "value1"})
print(response.text)