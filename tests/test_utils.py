import json
import os
import tempfile
import unittest
from typing import Any
from unittest.mock import mock_open, patch

import pytest

from src.utils import file_read

test_file_path = "test_operations.json"


def test_file_read_valid() -> None:
    """Тест на проверку работы функции"""
    valid_data = [{"operationAmount": {"currency": {"code": "EUR"}, "amount": "50.00"}}]
    with open(test_file_path, "w", encoding="utf-8") as f:
        json.dump(valid_data, f)

    result = file_read(test_file_path)
    assert result[0]["operationAmount"]["amount"] == "50.00"
    os.remove(test_file_path)


@pytest.mark.parametrize("files, expected", [("", []), ({}, []), ("C:/Users/VIP/my_prj/bank/data/operations.jso", [])])
def test_file_read_invalid(files: Any, expected: list) -> None:
    """Если файл не задан, пустой файл, некорректные данные"""
    assert file_read(files) == expected


@patch("builtins.open", new_callable=mock_open, read_data='[{"amount": 100, "currency": "USD"}]')
def test_valid_file(mock_file: Any) -> None:
    """Корректная работа функции с мок"""
    transactions = file_read("data/operations.json")
    assert transactions == [{"amount": 100, "currency": "USD"}]


@patch("builtins.open", new_callable=mock_open, read_data='{"amount": 100}')
def test_not_a_list(mock_file: Any) -> None:
    """Если в файле некорректные данные (мок)"""
    transactions = file_read("data/operations.json")
    assert transactions == []


@patch("builtins.open", new_callable=mock_open, read_data="")
def test_empty_file(mock_file: Any) -> None:
    """Если файл не задан, пустой файл (мок)"""
    transactions = file_read("data/operations.json")
    assert transactions == []
