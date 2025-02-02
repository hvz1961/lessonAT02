def count_vowels(s):
    """
    Подсчитывает количество гласных в строке.

    :param s: Входная строка
    :return: Количество гласных в строке
    """
    vowels = "aeiouAEIOU"  # Все гласные (строчные и прописные)
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

