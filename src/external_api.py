
import os

import requests
from dotenv import load_dotenv


def conversion(list_transactions: list) -> float:
    """Функция, которая принимает на вход транзакцию и возвращает сумму транзакции"""
    if not list_transactions:
        raise ValueError("the list is empty")
    else:
        for i in list_transactions:
            if i["operationAmount"]["currency"]["code"] == "RUB":
                return float(i["operationAmount"]["amount"])
            else:
                currency = i["operationAmount"]["currency"]["code"]
                amount = i["operationAmount"]["amount"]
                load_dotenv()
                headers = {"apikey": os.getenv("API_KEY")}
                response = requests.get(
                    f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}",
                    headers=headers,
                )
                if response.status_code != 200:
                    raise ValueError("Failed to get amount transactions")
                else:
                    return float(response.json()["result"])
