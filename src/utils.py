import json
from json import JSONDecodeError


def file_read(file='C:/Users/VIP/my_prj/bank/data/operations.json'):
    try:
        list_ = []
        if file:
            with open(file, 'r', encoding="utf-8") as f:
                operations = json.load(f)
                if len(operations) == 0 or type(operations) != list:
                    return list_
                return operations
        if not file:
                return list_
    except FileNotFoundError:
        return []
    except JSONDecodeError:
        return []
