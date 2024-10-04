import tempfile
from typing import Any

from src.decorators import log


def test_log_good() -> None:
    """Тестирует выполнение декорированной функции"""

    def my_function(x: int, y: int) -> int:
        return x + y

    result = my_function(1, 2)
    assert result == 3


def test_log_txt() -> None:
    """Тестирует запись в файл после успешного выполнения"""
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        log_file_path = tmp_file.name

    @log(filename_=log_file_path)
    def my_function(x: int, y: int) -> int:
        return x + y

    my_function(1, 2)
    with open(log_file_path, "r", encoding="utf-8") as file:
        text = file.read()
        assert "my_function ok\nstart my_function\nresult: 3\nend my_function" in text


def test_log_txt_error() -> None:
    """Тестирует запись в файл при ошибке"""
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        log_file_path = tmp_file.name

    @log(filename_=log_file_path)
    def my_function(x: int, y: int) -> int:
        return x + y

    my_function(1, "2")
    with open(log_file_path, "r", encoding="utf-8") as file:
        text = file.read()
        assert "my_function error: unsupported operand type(s) for +: 'int' and 'str'. Inputs: ((1, '2'), {})" in text


def test_log_caps_with_filename(capsys: Any) -> None:
    """Тестирует вывод в консоль, если есть файл и функция работает"""
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        log_file_path = tmp_file.name

    @log(filename_=log_file_path)
    def my_function(x: int, y: int) -> int:
        return x + y

    my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == ""


def test_log_caps_with_filename_invalid(capsys: Any) -> None:
    """Тестирует вывод в консоль, если есть файл и функция не работает"""
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        log_file_path = tmp_file.name

    @log(filename_=log_file_path)
    def my_function(x: int, y: int) -> int:
        return x + y

    my_function(1, "2")
    captured = capsys.readouterr()
    assert captured.out == ""


def test_log_caps_without_filename(capsys: Any) -> None:
    """Тестирует вывод в консоль, если нет файла и функция работает"""

    @log(filename_="")
    def my_function(x: int, y: int) -> int:
        return x + y

    my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\nstart my_function\nresult: 3\nend my_function\n"


def test_log_caps_without_filename_invalid(capsys: Any) -> None:
    """Тестирует вывод в консоль, если нет файла и функция не работает"""

    @log(filename_="")
    def my_function(x: int, y: int) -> int:
        return x + y

    my_function(1, "2")
    captured = capsys.readouterr()
    assert (
        captured.out
        == "my_function error: unsupported operand type(s) for +: 'int' and 'str'. Inputs: ((1, '2'), {})\n"
    )
