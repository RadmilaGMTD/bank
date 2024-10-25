def filter_by_state(list_of_dictionaries: list, optional_value: str = "EXECUTED") -> list:
    """Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению."""
    new_list = []
    for i in list_of_dictionaries:
        if i.get("state") == optional_value:
            new_list.append(i)
    return new_list


def sort_by_date(list_of_dictionaries: list, sort_parameter: bool = True) -> list:
    """Функция возвращает новый список, отсортированный по дате."""
    sorted_list = sorted(list_of_dictionaries, key=lambda i: i.get("date", "0"), reverse=sort_parameter)
    return sorted_list
