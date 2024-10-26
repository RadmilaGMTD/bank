import csv
import json
import os
from unittest.mock import patch

import pandas as pd
import pytest

from src.users import filter_currency, result, user_file, user_filter, user_sort

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
file_path_json = os.path.join(project_root, "data", "operations.json")
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
test_file_path_csv = os.path.join(project_root, "data", "test_transactions.csv")
test_file_path_excel = os.path.join(project_root, "data", "test_transactions_excel.xlsx")
test_file_path = "test_operations.json"


def test_user_file_json() -> None:
    expected_data = [
        {
            "date": "2019-08-26T10:50:58.294041",
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "id": 441945886,
        },
        {
            "date": "2019-07-03T18:35:29.512364",
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "id": 41428829,
        },
    ]
    with open(test_file_path, "w", encoding="utf-8") as f:
        json.dump(expected_data, f)
    with patch("builtins.print") as mock_print:
        result = user_file("1", test_file_path, "dummy.csv", "dummy.xlsx")
        mock_print.assert_called_once_with("Для обработки выбран JSON-файл.")
        assert result == expected_data
        os.remove(test_file_path)


def test_user_file_csv() -> None:
    rows = [{"id": 650703.0, "state": "EXECUTED", "date": "2023-09-05T11:30:32Z"}]
    with open(test_file_path_csv, "w", encoding="utf-8", newline="") as f:
        fieldnames = ["id", "state", "date"]
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=";")
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
    with patch("builtins.print") as mock_print:
        result = user_file("2", "dummy.json", test_file_path_csv, "dummy.xlsx")
        mock_print.assert_called_once_with("Для обработки выбран CSV-файл.")
        assert result == rows
        os.remove(test_file_path_csv)


def test_user_file_excel() -> None:
    rows = [{"id": 650703.0, "state": "EXECUTED", "date": "2023-09-05T11:30:32Z"}]
    df = pd.DataFrame(rows)
    df.to_excel(test_file_path_excel, index=False)
    with patch("builtins.print") as mock_print:
        result = user_file(
            "3",
            "dummy.json",
            "dummy.csv",
            test_file_path_excel,
        )
        mock_print.assert_called_once_with("Для обработки выбран XLSX-файл.")
        assert result == rows
        os.remove(test_file_path_excel)


def test_user_file_invalid() -> None:
    rows = [{"id": 650703.0, "state": "EXECUTED", "date": "2023-09-05T11:30:32Z"}]
    df = pd.DataFrame(rows)
    df.to_excel(test_file_path_excel, index=False)
    with pytest.raises(ValueError):
        user_file("4", "dummy.json", "dummy.csv", test_file_path_excel)
    os.remove(test_file_path_excel)


@pytest.fixture()
def transactions():
    return [
        {"operationAmount": {"value": 100, "currency": {"code": "RUB"}}, "description": "Транзакция 1"},
        {"operationAmount": {"value": 200, "currency": {"code": "USD"}}, "description": "Транзакция 2"},
        {"operationAmount": {"value": 150, "currency": {"code": "RUB"}}, "description": "Транзакция 3"},
    ]


def test_filter_currency_yes(transactions) -> None:
    filtered_result = filter_currency("да", transactions)
    assert filtered_result == [
        {"operationAmount": {"value": 100, "currency": {"code": "RUB"}}, "description": "Транзакция 1"},
        {"operationAmount": {"value": 150, "currency": {"code": "RUB"}}, "description": "Транзакция 3"},
    ]


def test_filter_currency_no(transactions) -> None:
    filtered_result_no = filter_currency("нет", transactions)
    assert filtered_result_no == transactions


def test_filter_currency_invalid() -> None:
    transactions = [{"operationAmount": {"value": 200, "currency": {"code": "USD"}}, "description": "Транзакция 2"}]
    filtered_result_invalid = filter_currency("да", transactions)
    assert filtered_result_invalid == []


def test_user_sort() -> None:
    transactions = [
        {"date": "2023-10-01", "amount": 100},
        {"date": "2023-09-01", "amount": 200},
        {"date": "2023-08-01", "amount": 300},
    ]
    with patch("builtins.input", side_effect=["по возрастанию"]):
        sorted_result = user_sort(transactions, "да")
        assert sorted_result == [
            {"date": "2023-08-01", "amount": 300},
            {"date": "2023-09-01", "amount": 200},
            {"date": "2023-10-01", "amount": 100},
        ]
    with patch("builtins.input", side_effect=["по убыванию"]):
        sorted_result_desc = user_sort(transactions, "да")
        assert sorted_result_desc == [
            {"date": "2023-10-01", "amount": 100},
            {"date": "2023-09-01", "amount": 200},
            {"date": "2023-08-01", "amount": 300},
        ]
    sorted_result_no = user_sort(transactions, "нет")
    assert sorted_result_no == transactions


def test_user_filter(transactions) -> None:
    with patch("builtins.input", side_effect=["Транзакция 1"]):
        filter_result = user_filter(
            "да",
            transactions,
        )
        assert filter_result == [
            {"operationAmount": {"value": 100, "currency": {"code": "RUB"}}, "description": "Транзакция 1"}
        ]
    filter_result_no = user_filter("нет", transactions)
    assert filter_result_no == transactions


def test_result() -> None:
    transactions_1 = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        }
    ]
    result_result_1 = result(transactions_1, "1")
    assert next(result_result_1) == "26.08.2019 Перевод организации \n1596 83** **** 5199 -> **9589 \nСумма: 31957.58"

    transactions_2 = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "amount": "31957.58",
            "currency": {"name": "руб.", "code": "RUB"},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        }
    ]
    result_result_2 = result(transactions_2, "2")
    assert next(result_result_2) == "26.08.2019 Перевод организации \n1596 83** **** 5199 -> **9589 \nСумма: 31957.58"
