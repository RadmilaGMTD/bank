from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(info_and_number: str) -> str:
    """Функция, которая маскирует номер карты или счёта"""
    if len(info_and_number) > 0:
        if info_and_number.isdigit() or info_and_number.isalpha():
            raise ValueError("Неправильный номер карты или счета")
        info_and_number_split = info_and_number.split()
        for info_and_number_i in info_and_number_split:
            if info_and_number_i.isdigit():
                if len(info_and_number_i) == 16:
                    return get_mask_card_number(info_and_number_i)
                elif len(info_and_number_i) == 20:
                    return get_mask_account(info_and_number_i)
                raise ValueError("Неправильный номер карты или счета")
    raise ValueError("Неправильный номер карты или счета")


def get_date(user_data: str) -> str:
    """Функция, которая выводит дату"""
    if len(user_data) > 0:
        user_data_split = user_data[:10].split("-")
        result = ".".join(user_data_split[::-1])
        if "0" < result[:2] <= "31" and "0" < result[3:5] <= "12":
            return result
        raise ValueError("Некорректный ввод")
    raise ValueError ("Пустая строка")

