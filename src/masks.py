def get_mask_card_number(card_number: str) -> str:
    """Функция, которая маскирует номер карты"""
    if len(card_number) < 16 or len(card_number) > 16:
        raise ValueError("Неправильный номер карты")
    elif card_number.isdigit():
        new_card_number = ""
        new_card_number += card_number[:4]
        new_card_number += " "
        new_card_number += card_number[4:6]
        new_card_number += "** **** "
        new_card_number += card_number[12:]
        return new_card_number
    raise ValueError("Неправильный номер карты")


def get_mask_account(account_number: str) -> str:
    """Функция, которая маскирует номер счета"""
    if len(account_number) < 20 or len(account_number) > 20:
        raise ValueError("Неправильный номер счета")
    elif account_number.isdigit():
        new_account_number = ""
        new_account_number += "**"
        new_account_number += account_number[-4:]
        return new_account_number
    raise ValueError("Неправильный номер счета")
