# bank
## Это виджет, который показывает несколько последних успешных банковских операций клиента. Проект, который на бэкенде будет готовить данные для отображения в новом виджете.
## Установка
1. Клонируйте репозиторий:
```
git@github.com:RadmilaGMTD/bank.git
```
2. Установите зависимости:
```
poetry install
```
## Использование
1. Для того чтобы замаскировать счёт или номер карты, воспользуйтесь функцией mask_account_card. Пример результата: "Visa Platinum 7000 79** **** 6361" или "Счет **4305")
2. Для того чтобы получить дату, воспользуйтесь get_date.
3. Для того чтобы отсортировать словари по ключевому слову, используйте filter_by_state.
4. Для того чтобы отсортировать список по дате, воспользуйтесь функцией sort_by_date.
5. Для того чтобы получить поочередно транзакции, используйте функцию filter_by_currency.
6. Чтобы получить описания по транзакциям, воспользуйтесь transaction_descriptions.
## Декоратор
### Декоратор @log, который выводит логи(начало, результат, конец функции) в консоль или в файл
## Тестирование
### В проекте применяется фреймворк тестирования pytest. Для его использование необходимо:
1. Установить pytest:
```
poetry add --group dev pytest
```
2. Чтобы запустить тесты с оценкой покрытия:
```
pytest --cov
```
3. Отчет будет сгенерирован в папке htmlcov и храниться в файле с названием index.html.