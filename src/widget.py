from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(info_and_number: str) -> str:
    """Функция, которая маскирует номер карты или счёта"""
    info_and_number_split = info_and_number.split()
    for info_and_number_i in info_and_number_split:
        if info_and_number_i.isdigit():
            if len(info_and_number_i) == 16:
                result = get_mask_card_number(info_and_number_i)
            elif len(info_and_number_i) == 20:
                result = get_mask_account(info_and_number_i)
    return result


def get_date(user_data: str) -> str:
    """Функция, которая выводит дату"""
    user_data_split = user_data[:10].split("-")
    return ".".join(user_data_split[::-1])
