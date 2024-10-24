import logging
import os

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))  # поднимаемся на один уровень выше
log_directory = os.path.join(project_root, "logs")  # Папка logs в корне проекта
log_file_path = os.path.join(log_directory, "masks.log")
file_handler = logging.FileHandler(log_file_path, "w", encoding="utf-8")
file_formate = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formate)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Функция, которая маскирует номер карты"""
    logger.info("Проверяем номер карты")
    if len(card_number) < 16 or len(card_number) > 16:
        logger.error("Неправильный номер карты")
        raise ValueError("Неправильный номер карты")
    elif card_number.isdigit():
        new_card_number = ""
        new_card_number += card_number[:4]
        new_card_number += " "
        new_card_number += card_number[4:6]
        new_card_number += "** **** "
        new_card_number += card_number[12:]
        return new_card_number
    raise ValueError("Неправильный номер карты")


def get_mask_account(account_number: str) -> str:
    """Функция, которая маскирует номер счета"""
    logger.info("Проверяем номер счета")
    if len(account_number) < 20 or len(account_number) > 20:
        logger.error("Неправильный номер счета")
        raise ValueError("Неправильный номер счета")
    elif account_number.isdigit():
        new_account_number = ""
        new_account_number += "**"
        new_account_number += account_number[-4:]
        return new_account_number
    raise ValueError("Неправильный номер счета")
