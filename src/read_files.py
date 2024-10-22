import csv
import pandas as pd
from typing import Any


def read_csv(file: Any = None) -> list:
    '''Функция, для чтения csv файла'''
    file_read_csv = pd.read_csv(file, delimiter=";")
    return file_read_csv.to_dict(orient='records')


def read_excel(file: Any = None) -> list:
    '''Функция, для чтения excel файла'''
    file_read_xlsx = pd.read_excel(file)
    return file_read_xlsx.to_dict(orient='records')
