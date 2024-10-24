import re
from collections import Counter


def filter_transaction(list_dict: list, description_value: str) -> list:
    result = [transaction for transaction in list_dict if re.match(description_value, transaction['description'])]
    return result


def count_transaction(list_dict: list, list_description: list) -> dict:
    category = [description['description'] for description in list_dict if description['description'] in list_description]
    return Counter(category)


if __name__ == '__main__':
    list_trans = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 142264268,
        "state": "CANCELED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 142264268,
        "state": "CANCELED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }
]
    user_description_input = input()
    fun = filter_transaction(list_trans, user_description_input)
    print(fun)
    list_category = ["Перевод организации", "Перевод со счета на счет", "Открытие вклада", "Перевод с карты на карту"]
    fun_2 = count_transaction(list_trans, list_category)
    print(fun_2)