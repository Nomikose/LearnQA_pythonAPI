import json


string_as_json_format = '{"answer": "Hello, mr. Anderson"}'
obj = json.loads(string_as_json_format)

key = 'answer'
# string_as_json_format = '{"answer": "Hello, User"}'
# obj = json.loads(string_as_json_format)
# print(obj['answer'])

# key2 = "answer2"
# 423d22c3fae17300ad425fdcf8ea858fe04c1af4

if key in obj:
    print(obj[key])
else:
    print(f"Ключа {key} в JSON нет")
# 423d22c3fae17300ad425fdcf8ea858fe04c1af4

# Codes:
# 100 - 199 информационные
# 200 - 299 успех
# 300 - 399 перенаправление
# 400 - 499 ошибка клиента
# 500 - 599 ошибка сервера