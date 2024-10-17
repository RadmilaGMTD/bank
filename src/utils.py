import json
from json import JSONDecodeError
from typing import Any


def file_read(file: Any = "C:/Users/VIP/my_prj/bank/data/operations.json") -> list:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях."""
    try:
        if file:
            with open(file, "r", encoding="utf-8") as f:
                operations = json.load(f)
                if len(operations) == 0 or not isinstance(operations, list):
                    return []
                return operations
        if not file:
            return []
    except (FileNotFoundError, JSONDecodeError):
        return []
    return []  # Добавила, чтобы mypy не показывал ошибку
