def get_mask_card_number(card_number: str) -> str:
    """Функция, которая маскирует номер карты"""
    new_card_number = ""
    new_card_number += card_number[:4]
    new_card_number += " "
    new_card_number += card_number[4:6]
    new_card_number += "** **** "
    new_card_number += card_number[12:]
    return new_card_number


print(get_mask_card_number("7000792289606361"))


def get_mask_account(account_number: str) -> str:
    """Функция, которая маскирует номер счета"""
    new_account_number = ""
    new_account_number += "**"
    new_account_number += account_number[-4:]
    return new_account_number


print(get_mask_account("73654108430135874305"))
