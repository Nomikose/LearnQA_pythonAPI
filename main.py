from json.decoder import JSONDecodeError
import requests

# HEAD
# Get запрос - нет тела, но могут быть переданы параметры в строке запроса через ?
# payload = {"name": "Sam"}
# response = requests.get("https://playground.learnqa.ru/api/hello", params=payload)
# print(response.text)


# Обрабатываем ошибку с парсингом ответа
# payload = {"name": "Vanya"}
# response = requests.get("https://playground.learnqa.ru/api/hello", params=payload)
# print(response.text)
#
response = requests.get("https://playground.learnqa.ru/api/hello", params={"name": "Jhon"})
parsed_response_text = response.json()
print(parsed_response_text["answer"])
#
# #Модулятор нашего исключения, закомментируй get_text и получишь исключение
# #response = requests.get("https://playground.learnqa.ru/api/get_text")
# print(response.text)
#
try:
    parsed_response_text = response.json()
    print(parsed_response_text)
except JSONDecodeError:
    print("Response is not a JSON format")

# Инфа внутри post'a
# response = requests.post("https://playground.learnqa.ru/api/check_type", data={"param1": "value1"})
# print(response.text)


# Смотрим редирект по 301 коду ответа, а также вытаскиваем инфу из массива history
# response = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=True)
# # print(response.status_code)
# # print(response.text)
#
# first_response = response.history[0]
# second_response = response
# print(first_response.url)
# print(second_response.url)

# Смотрим заголовки
# headers = {"some_header": "123"}
# response = requests.get("https://playground.learnqa.ru/api/show_all_headers", headers = headers)
# print(response.text)
# print(response.headers)

# Изучаем cookie's
# payload = {"login": "secret_login", "password": "secret_pass"}
# response1 = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data = payload)
# print(response1.text)
# print(response1.status_code)
# print(dict(response1.cookies))
#
# cookie_value = response1.cookies.get("auth_cookie")
#
# cookies = {}
# if cookie_value is not None:
#     cookies.update({"auth_cookie": cookie_value})
#
# response2 = requests.post("https://playground.learnqa.ru/api/check_auth_cookie", cookies = cookies)
# print(response2.text)


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
# 423d22c3fae17300ad425fdcf8ea858fe04c1af4
