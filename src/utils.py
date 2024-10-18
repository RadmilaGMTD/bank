import json
from json import JSONDecodeError
from typing import Any
import logging

logger = logging.getLogger('utils')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('logs/utils.log','w',encoding='utf-8')
file_formate = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formate)
logger.addHandler(file_handler)


def file_read(file: Any = "C:/Users/VIP/my_prj/bank/data/operations.json") -> list:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях."""
    try:
        logger.info(f'Проверяем наличие файла {file}')
        if file:
            logger.info(f'Записываем в файл {file}')
            with open(file, "r", encoding="utf-8") as f:
                operations = json.load(f)
                if len(operations) == 0 or not isinstance(operations, list):
                    return []
                return operations
        if not file:
            return []
    except (FileNotFoundError, JSONDecodeError):
        logger.error('Файл не найден')
        return []
    return []  # Добавила, чтобы mypy не показывал ошибку
