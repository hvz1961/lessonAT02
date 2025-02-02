import pytest
from main import count_vowels

# Тест 1: Строка, содержащая только гласные
def test_all_vowels():
    assert count_vowels("aeiou") == 5
    assert count_vowels("AEIOU") == 5
    assert count_vowels("aAeEiIoOuU") == 10
# Тест 2: Строка без гласных
def test_no_vowels():
    assert count_vowels("bcdfg") == 0
    assert count_vowels("12345!@#") == 0
    assert count_vowels("") == 0  # Пустая строка
# Тест 3: Смешанная строка (гласные и согласные, прописные и строчные)
def test_mixed_string():
    assert count_vowels("Hello, World!") == 3
    assert count_vowels("Python is awesome") == 6
    assert count_vowels("ThE qUiCk BrOwN fOx") == 5
# Тест 4: Проверка на нестроковые входные данные (должно вызывать исключение)
def test_non_string_input():
    with pytest.raises(TypeError):
        count_vowels(123)  # Передаём число вместо строки

