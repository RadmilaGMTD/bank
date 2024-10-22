import csv
import pandas as pd
from typing import Any


def read_csv(file: Any = None) -> list:
    list_dict_trans = file.to_dict(orient='records')
    return list_dict_trans


def read_excel(file: Any = None) -> list:
    list_dict_trans = file.to_dict(orient='records')
    return list_dict_trans


if __name__ == '__main__':
    file_read_csv = pd.read_csv('../data/transactions.csv', delimiter=";")
    print(read_csv(file_read_csv))
    file_read_xlsx = pd.read_excel('../data/transactions_excel.xlsx')
    print(read_excel(file_read_xlsx))


