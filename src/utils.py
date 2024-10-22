import json
import logging
import os
from json import JSONDecodeError


logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
log_directory = os.path.join(project_root, "logs")
log_file_path = os.path.join(log_directory, "utils.log")
file_handler = logging.FileHandler(log_file_path, "w", encoding="utf-8")
file_format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_format)
logger.addHandler(file_handler)


def file_read(file: str) -> list:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях."""
    try:
        logger.info(f"Проверяем наличие файла {file}")
        if file:
            logger.info(f"Записываем в файл {file}")
            with open(file, "r", encoding="utf-8") as f:
                operations = json.load(f)
                if not isinstance(operations, list):
                    return []
                return operations
        if not file:
            logger.warning("Путь к файлу не указан.")
            return []
    except (FileNotFoundError, JSONDecodeError):
        logger.error("Файл не найден")
        return []
    except JSONDecodeError:
        logger.error("Ошибка декодирования JSON; файл может быть поврежден или содержать некорректные данные.")
    return []  # Добавила, чтобы mypy не показывал ошибку
