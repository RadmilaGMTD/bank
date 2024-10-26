import os
# from src.read_files import read_csv, read_excel
# from src.utils import file_read
# from src.widget import get_date, mask_account_card
# import re
from typing import Iterator

# from src.external_api import conversion
# from src.filter_count import filter_transaction
# from src.generators import card_number_generator, filter_by_currency, transaction_descriptions
from src.processing import filter_by_state
from src.users import filter_currency, result, user_file, user_filter, user_sort

# print(mask_account_card("Maestro 1596837868705199"))
# print(get_date("2024-03-11T02:26:18.671407"))
# print(
#     filter_by_state(
#         [
#             {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#             {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#             {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#             {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#         ],
#         "EXECUTED",
#     )
# )
# print(
#     sort_by_date(
#         [
#             {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#             {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#             {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#             {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#         ],
#         True,
#     )
# )
#
#
# transactions = [
#     {
#         "id": 939719570,
#         "state": "EXECUTED",
#         "date": "2018-06-30T02:08:58.425572",
#         "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
#         "description": "Перевод организации",
#         "from": "Счет 75106830613657916952",
#         "to": "Счет 11776614605963066702",
#     },
#     {
#         "id": 142264268,
#         "state": "EXECUTED",
#         "date": "2019-04-04T23:20:05.206878",
#         "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
#         "description": "Перевод со счета на счет",
#         "from": "Счет 19708645243227258542",
#         "to": "Счет 75651667383060284188",
#     },
# ]
# usd_transactions = filter_by_currency(transactions)
# for n in range(2):
#     print(next(usd_transactions))
#
# transactions_2 = [
#     {
#         "id": 939719570,
#         "state": "EXECUTED",
#         "date": "2018-06-30T02:08:58.425572",
#         "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
#         "description": "Перевод организации",
#         "from": "Счет 75106830613657916952",
#         "to": "Счет 11776614605963066702",
#     },
#     {
#         "id": 142264268,
#         "state": "EXECUTED",
#         "date": "2019-04-04T23:20:05.206878",
#         "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
#         "description": "Перевод со счета на счет",
#         "from": "Счет 19708645243227258542",
#         "to": "Счет 75651667383060284188",
#     },
#     {
#         "id": 142264268,
#         "state": "EXECUTED",
#         "date": "2019-04-04T23:20:05.206878",
#         "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
#         "description": "Перевод со счета на счет",
#         "from": "Счет 19708645243227258542",
#         "to": "Счет 75651667383060284188",
#     },
#     {
#         "id": 142264268,
#         "state": "EXECUTED",
#         "date": "2019-04-04T23:20:05.206878",
#         "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
#         "description": "Перевод с карты на карту",
#         "from": "Счет 19708645243227258542",
#         "to": "Счет 75651667383060284188",
#     },
#     {
#         "id": 142264268,
#         "state": "EXECUTED",
#         "date": "2019-04-04T23:20:05.206878",
#         "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
#         "description": "Перевод организации",
#         "from": "Счет 19708645243227258542",
#         "to": "Счет 75651667383060284188",
#     },
# ]
#
#
# descriptions = transaction_descriptions(transactions_2)
# for i in range(5):
#     print(next(descriptions))
#
#
# gen = card_number_generator(1, 5)
# for card_number in card_number_generator(1, 5):
#     print(next(gen))
#
#
# project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
# file = os.path.join(project_root, "bank", "data", "operations.json")
#
# fun = file_read(file)
# print(fun)
#
#
# list_transactions = file_read(file)
# func = conversion(list_transactions)
# print(func)
#
#
# file_csv = os.path.join(project_root, "bank", "data", "transactions.csv")
# print(read_csv(file_csv))


# file_excel = os.path.join(project_root, "bank", "data", "transactions_excel.xlsx")
# print(read_excel(file_excel))

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
file_json = os.path.join(project_root, "bank", "data", "operations.json")
file_csv = os.path.join(project_root, "bank", "data", "transactions.csv")
file_excel = os.path.join(project_root, "bank", "data", "transactions_excel.xlsx")


def main() -> Iterator:
    """Функция, которая отвечает за основную логику проекта с пользователем"""
    user_input = input(
        "Привет! Добро пожаловать в программу работы с банковскими транзакциями.\nВыберите необходимый пункт меню:\n1. Получить информацию о транзакциях из JSON-файла\n2. Получить информацию о транзакциях из CSV-файла\n3. Получить информацию о транзакциях из XLSX-файла\nВыберите формат файла: "
    )
    result_user_file = user_file(user_input, file_json, file_csv, file_excel)
    while True:
        user_input_2 = (
            input(
                "Введите статус, по которому необходимо выполнить фильтрацию.\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING: "
            )
            .strip()
            .upper()
        )
        if user_input_2 in ("EXECUTED", "CANCELED", "PENDING"):
            break
        else:
            print(f"Статус операции {user_input_2} недоступен.")
    result_filter_by_state = filter_by_state(result_user_file, user_input_2)
    if not result_filter_by_state:
        print(f"Транзакции по статусу {user_input_2} не найдены")
        return
    print(f"Операции отфильтрованы по статусу {user_input_2}")
    user_input_3 = input("Отсортировать операции по дате? Да/Нет: ").strip().lower()
    result_user_sort = user_sort(result_filter_by_state, user_input_3)
    user_input_5 = input("Выводить только рублевые транзакции? Да/Нет: ").strip().lower()
    result_filter_currency = filter_currency(user_input_5, result_user_sort, "RUB")
    if not result_filter_currency:
        print("Рублевые транзакции не найдены")
        return
    user_input_6 = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ").strip().lower()
    result_user_filter = user_filter(user_input_6, result_filter_currency)
    result_function = result(result_user_filter, user_input)
    if len(result_user_filter) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return
    print(f"Всего банковских операций в выборке: {len(result_user_filter)}")
    for d in range((len(result_user_filter) - 1)):
        print(next(result_function))


main()
