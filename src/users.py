import re
from typing import Any

from src.filter_count import filter_transaction
from src.processing import sort_by_date
from src.read_files import read_csv, read_excel
from src.utils import file_read
from src.widget import get_date, mask_account_card


def user_file(user_input_file: str, json: str, csv: str, excel: str) -> list:
    """Пользователь выбирает файл"""
    if user_input_file == "1":
        print("Для обработки выбран JSON-файл.")
        return file_read(json)
    elif user_input_file == "2":
        print("Для обработки выбран CSV-файл.")
        return read_csv(csv)
    elif user_input_file == "3":
        print("Для обработки выбран XLSX-файл.")
        return read_excel(excel)
    else:
        raise ValueError("Неправильный ввод")


def user_sort(list_dict: list, user_answer: str) -> list:
    """Пользователь делает выбор по наличию сортировки и виду сортировки"""
    if user_answer == "да":
        user_input_4 = input("Отсортировать по возрастанию или по убыванию?: ").strip().lower()
        if user_input_4 == "по возрастанию":
            return sort_by_date(list_dict, False)
        elif user_input_4 == "по убыванию":
            return sort_by_date(list_dict, True)
    elif user_answer == "нет":
        return list_dict


def filter_currency(user_answer: str, result_list_sort_by_date: list, currency_value: str = "RUB") -> list:
    """Пользователь делает выбор о рублевых транзакциях"""
    if user_answer == "да":
        return [
            currency
            for currency in result_list_sort_by_date
            if re.match(
                currency_value,
                currency.get("operationAmount").get("currency").get("code") or currency.get("currency_code"),
            )
        ]
    elif user_answer == "нет":
        return result_list_sort_by_date
    return []


def user_filter(user_answer: str, list_dict: list) -> list:
    """Пользователь делает выбор о фильтрации транзакций по описанию"""
    if user_answer == "да":
        user_input_7 = input("Введите описание операции: ")
        result_filter_transactions = filter_transaction(list_dict, user_input_7)
        print("Распечатываю итоговый список транзакций")
        return result_filter_transactions
    elif user_answer == "нет":
        return list_dict


def result(result_list: list, user_input_1: str) -> Any:
    """Итоговая функция, которая выводит все отфильтрованные пользователем транзакции"""
    for i in result_list:
        data_ = get_date(i["date"])
        category = i.get("description")
        from_ = mask_account_card(i.get("from", ""))
        to_ = mask_account_card(i.get("to", ""))
        if user_input_1 == "1":
            amount = i.get("operationAmount", {}).get("amount", 0)
        elif user_input_1 == "2" or user_input_1 == "3":
            amount = i.get("amount", 0)
        yield f"{data_} {category} \n{from_} -> {to_} \nСумма: {amount}"
