import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture()
def transactions() -> list:
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
    ]


@pytest.fixture()
def currency_() -> str:
    return "RUB"


def test_filter_by_currency(transactions: list) -> None:
    usd_transactions = filter_by_currency(transactions, "USD")
    assert next(usd_transactions) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(usd_transactions) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }


def test_filter_by_currency_not_currency(transactions: list, currency_: str) -> None:
    with pytest.raises(ValueError):
        usd_transactions = filter_by_currency(transactions, currency_)
        next(usd_transactions)


def test_filter_by_currency_not_list(currency_: str) -> None:
    with pytest.raises(ValueError):
        usd_transactions = filter_by_currency([], currency_)
        next(usd_transactions)


@pytest.mark.parametrize(
    "list_of_dict, cur, expected_1, expected_2",
    [
        (
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "RUB", "code": "RUB"}},
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                },
                {
                    "id": 142264268,
                    "state": "EXECUTED",
                    "date": "2019-04-04T23:20:05.206878",
                    "operationAmount": {"amount": "79114.93", "currency": {"name": "RUB", "code": "RUB"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                },
            ],
            "RUB",
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {"amount": "9824.07", "currency": {"name": "RUB", "code": "RUB"}},
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702",
            },
            {
                "id": 142264268,
                "state": "EXECUTED",
                "date": "2019-04-04T23:20:05.206878",
                "operationAmount": {"amount": "79114.93", "currency": {"name": "RUB", "code": "RUB"}},
                "description": "Перевод со счета на счет",
                "from": "Счет 19708645243227258542",
                "to": "Счет 75651667383060284188",
            },
        )
    ],
)
def test_filter_by_currency_(list_of_dict: list, cur: str, expected_1: dict, expected_2: dict) -> None:
    usd_transactions = filter_by_currency(list_of_dict, cur)
    assert next(usd_transactions) == expected_1
    assert next(usd_transactions) == expected_2


@pytest.fixture()
def transactions_2() -> list:
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
    ]


def test_transaction_descriptions(transactions: list) -> None:
    descriptions = transaction_descriptions(transactions)
    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод со счета на счет"


@pytest.mark.parametrize(
    "list_dict",
    (
        [
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {"amount": "9824.07", "currency": {"name": "RUB", "code": "RUB"}},
                "description": "",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702",
            }
        ],
        {},
    ),
)
def test_transaction_descriptions_invalid(list_dict: list) -> None:
    with pytest.raises(ValueError):
        descriptions = transaction_descriptions(list_dict)
        next(descriptions)


def test_transaction_descriptions_(transactions_2: list) -> None:
    descriptions = transaction_descriptions(transactions_2)
    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод с карты на карту"
    assert next(descriptions) == "Перевод с карты на карту"
    assert next(descriptions) == "Перевод со счета на счет"


def test_card_number_generator() -> None:
    result = list(card_number_generator(1, 5))
    assert result == ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003", "0000 0000 0000 0004"]


def test_card_number_generator_gen() -> None:
    gen = card_number_generator(1, 5)
    assert next(gen) == "0000 0000 0000 0001"
    assert next(gen) == "0000 0000 0000 0002"


@pytest.mark.parametrize(
    "start_, stop_, expected",
    [
        (
            0,
            6,
            [
                "0000 0000 0000 0000",
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
            ],
        ),
        (0, 0, []),
        (1, 1, []),
        (1, 2, ["0000 0000 0000 0001"]),
        (2, 1, []),
    ],
)
def test_card_number_generator_(start_: int, stop_: int, expected: list) -> None:
    result = list(card_number_generator(start_, stop_))
    assert result == expected
