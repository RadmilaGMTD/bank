from typing import Iterator


def filter_by_currency(list_dict: list, currency: str = 'USD') -> Iterator:
    '''Функция должна возвращать итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной.'''
    if len(list_dict) > 0:
        for dic in list_dict:
            if dic.get('operationAmount').get('currency').get('code') == currency:
                yield dic
        raise ValueError ('Нет такой валюты')
    raise ValueError ('Список пуст')

transactions = [{
          "id": 939719570,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "USD",
                  "code": "USD"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
      },
      {
              "id": 142264268,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:05.206878",
              "operationAmount": {
                  "amount": "79114.93",
                  "currency": {
                      "name": "USD",
                      "code": "USD"
                  }
              },
              "description": "Перевод со счета на счет",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
       }]
usd_transactions = filter_by_currency(transactions)
for n in range(2):
    print(next(usd_transactions))


transactions_2 = [{
          "id": 939719570,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "USD",
                  "code": "USD"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
      },
      {
              "id": 142264268,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:05.206878",
              "operationAmount": {
                  "amount": "79114.93",
                  "currency": {
                      "name": "USD",
                      "code": "USD"
                  }
              },
              "description": "Перевод со счета на счет",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
       }, {
              "id": 142264268,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:05.206878",
              "operationAmount": {
                  "amount": "79114.93",
                  "currency": {
                      "name": "USD",
                      "code": "USD"
                  }
              },
              "description": "Перевод со счета на счет",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
       }, {
              "id": 142264268,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:05.206878",
              "operationAmount": {
                  "amount": "79114.93",
                  "currency": {
                      "name": "USD",
                      "code": "USD"
                  }
              },
              "description": "Перевод с карты на карту",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
       }, {
              "id": 142264268,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:05.206878",
              "operationAmount": {
                  "amount": "79114.93",
                  "currency": {
                      "name": "USD",
                      "code": "USD"
                  }
              },
              "description": "Перевод организации",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
       }]

def transaction_descriptions(list_dict: list) -> Iterator:
    '''Функция принимает список словарей с транзакциями и возвращает описание каждой операции по очереди.'''
    if len(list_dict) > 0 :
        for dic in list_dict:
            if len(dic["description"]) > 0:
                yield dic["description"]
        raise ValueError ('Отсутствует описание')
    raise ValueError('Пустой список')


descriptions = transaction_descriptions(transactions_2)
for i in range(5):
    print(next(descriptions))


def card_number_generator(start: int, stop: int) -> Iterator:
    '''Функция, которая выдает номера банковских карт в формате XXXX XXXX XXXX XXXX'''
    for number in range(start, stop):
        number = str(number)
        while len(number) < 16:
            number = '0' + number
        yield f'{number[:4]} {number[4:8]} {number[8:12]} {number[12:]}'

gen = card_number_generator(1,5)
for card_number in card_number_generator(1, 5):
    print(next(gen))