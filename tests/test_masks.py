import pytest
from src.masks import get_mask_card_number, get_mask_account

@pytest.fixture()
def card_number():
    return '700079228960636, '', 700079228960636100, qwertyuiopasdfgh'

@pytest.fixture()
def account_number():
    return '7365410843013587430, '', 7365410843013587430500, qwertyuiopasdfghjklz'


def test_get_mask_card_number():
    assert get_mask_card_number('7000792289606361') == '7000 79** **** 6361'


def test_get_mask_card_number_invalid_number(card_number):
    with pytest.raises(ValueError):
        get_mask_card_number(card_number)


def test_get_mask_account():
    assert get_mask_account('73654108430135874305') == '**4305'


def test_get_mask_account_invalid_number(account_number):
    with pytest.raises(ValueError):
        get_mask_account(account_number)
