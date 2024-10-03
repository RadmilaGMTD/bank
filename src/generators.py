from typing import Iterator


def filter_by_currency(list_dict: list, currency: str = "USD") -> Iterator:
    """Функция должна возвращать итератор, который поочередно выдает транзакции."""
    if len(list_dict) > 0:
        for dic in list_dict:
            if dic.get("operationAmount").get("currency").get("code") == currency:
                yield dic
        raise ValueError("Нет такой валюты")
    raise ValueError("Список пуст")


def transaction_descriptions(list_dict: list) -> Iterator:
    """Функция принимает список словарей с транзакциями и возвращает описание каждой операции по очереди."""
    if len(list_dict) > 0:
        for dic in list_dict:
            if len(dic["description"]) > 0:
                yield dic["description"]
        raise ValueError("Отсутствует описание")
    raise ValueError("Пустой список")


def card_number_generator(start: int, stop: int) -> Iterator:
    """Функция, которая выдает номера банковских карт в формате XXXX XXXX XXXX XXXX"""
    for number in range(start, stop):
        all_number = str(number)
        while len(all_number) < 16:
            all_number = "0" + all_number
        yield f"{all_number[:4]} {all_number[4:8]} {all_number[8:12]} {all_number[12:]}"
