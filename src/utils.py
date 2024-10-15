import json

def file_read(file=None):
    list_ = []
    if file:
        with open(file, 'r', encoding="utf-8") as f:
            operations = json.load(f)
            if len(operations) == 0 or type(operations) != list:
                return list_
            return operations
    if not file:
            return list_


if __name__ == "__main__":
    file = 'C:/Users/VIP/my_prj/bank/data/operations.json'
    fun = file_read(file)
    print(fun)