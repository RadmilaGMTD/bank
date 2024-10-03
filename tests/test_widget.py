import pytest

from src.widget import get_date, mask_account_card


def test_mask_account_card_card() -> None:
    assert mask_account_card("Maestro 1596837868705199") == "1596 83** **** 5199"


def test_mask_account_card_account() -> None:
    assert mask_account_card("Счет 73654108430135874305") == "**4305"


@pytest.mark.parametrize(
    "number, expected",
    [
        ("Maestro 1596837868705199", "1596 83** **** 5199"),
        ("Visa Platinum 7000792289606361", "7000 79** **** 6361"),
        ("Счет 73654108430135874305", "**4305"),
    ],
)
def test_mask_account_card_different(number: str, expected: str) -> None:
    assert mask_account_card(number) == expected


@pytest.mark.parametrize(
    "number", ("Maestro 159683786", "Счет 7000792289606361000000", "", "1234567891234567", "qwertyuiiiqwerty")
)
def test_test_mask_account_card_invalid_number(number: str) -> None:
    with pytest.raises(ValueError):
        mask_account_card(number)


def test_get_date() -> None:
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"


@pytest.mark.parametrize("text", ("2024.03.11T02:26:18.671407", "", "32.03.2024", "11.13.2024"))
def test_get_data_invalid_text(text: str) -> None:
    with pytest.raises(ValueError):
        get_date(text)
