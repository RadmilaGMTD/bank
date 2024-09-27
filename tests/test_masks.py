import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number() -> None:
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"


@pytest.mark.parametrize(
    "card_number", ("", "700079228960636", "700079228960636100", "qwertyuiopasdfgh", "1234qwerty")
)
def test_get_mask_card_number_invalid_number(card_number: str) -> None:
    with pytest.raises(ValueError):
        get_mask_card_number(card_number)


def test_get_mask_account() -> None:
    assert get_mask_account("73654108430135874305") == "**4305"


@pytest.mark.parametrize(
    "account_number", ("", "736541084301358743", "7365410843013587430500", "qwertyuiopasdfghqwer", "1234qwerty")
)
def test_get_mask_account_invalid_number(account_number: str) -> None:
    with pytest.raises(ValueError):
        get_mask_account(account_number)
