import re
from collections import Counter


def filter_transaction(list_dict: list, description_value: str) -> list:
    """Функция для поиска в списке словарей операций по заданной строке"""
    result = [description for description in list_dict if re.match(description_value, description["description"])]
    return result


def count_transaction(list_dict: list, list_description: list) -> dict:
    """Функция для подсчета количества банковских операций определенного типа."""
    category = [
        description["description"] for description in list_dict if description["description"] in list_description
    ]
    return dict(Counter(category))
