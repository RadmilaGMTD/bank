import json
import os
from unittest.mock import Mock, patch

import pytest
import requests
from dotenv import load_dotenv

from src.external_api import conversion
from src.utils import file_read


def test_conversion() -> None:
    """Корректная работа функции"""
    assert conversion(file_read("C:/Users/VIP/my_prj/bank/data/operations.json")) == 31957.58


def test_conversion_not_file() -> None:
    """Если на входе пустой список"""
    with pytest.raises(ValueError):
        conversion(file_read(""))


@patch("src.external_api.requests.get")
@patch("src.utils.file_read")
def test_conversion_valid(mock_file_read: Mock, mock_get: Mock) -> None:
    """Если статус не 200"""
    mock_get.return_value.status_code = 500
    mock_get.return_value.json.return_value = {}
    mock_file_read.return_value = [{"operationAmount": {"currency": {"code": "USD"}, "amount": "100"}}]
    with pytest.raises(ValueError, match="Failed to get amount transactions"):
        conversion(mock_file_read())


@patch("src.external_api.requests.get")
@patch("src.utils.file_read")
def test_conversion_invalid(mock_file_read: Mock, mock_get: Mock) -> None:
    """Если на входе пустой список (мок)"""
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {}
    mock_file_read.return_value = []
    with pytest.raises(ValueError, match="the list is empty"):
        conversion(mock_file_read())


@patch("src.external_api.requests.get")
@patch("src.utils.file_read")
def test_conversion_valid_rub(mock_file_read: Mock, mock_get: Mock) -> None:
    """Корректная работа функции (мок) (на входе рубли)"""
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {}
    mock_file_read.return_value = [{"operationAmount": {"currency": {"code": "RUB"}, "amount": "100"}}]
    assert conversion(mock_file_read()) == 100


@patch("src.external_api.requests.get")
@patch("src.utils.file_read")
def test_conversion_invalid(mock_file_read: Mock, mock_get: Mock) -> None:
    """Корректная работа функции (мок) (на входе usd)"""
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 3724.305775}
    mock_file_read.return_value = [{"operationAmount": {"currency": {"code": "USD"}, "amount": "100"}}]
    assert conversion(mock_file_read()) == 3724.305775
