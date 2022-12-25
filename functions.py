def get_prime_factors(n: int):
    if is_natural(n):
        divisor = 2
        lst = []
        while divisor <= n:
            if n % divisor == 0:
                lst.append(divisor)
                n = n // divisor
            else:
                divisor += 1
        return lst
    else:
        print(f'{n} not natural number!')


def is_natural(n):
    return isinstance(n, int) and n >= 1


def is_even(n: int):
    if isinstance(n, int):
        return True if n % 2 == 0 else False
    else:
        print(f'{n} not integer')


def check_remainder(n, divisor):
    """
    Прорека остатка от деления, например, проверка четности, это check_remainder(4, 2) -> True

    :param n: Число остаток от деления которого будим проверять
    :param divisor: Делитель числа n
    :return: True - если остаток от деления равен нулю или
            False - если остаток от деления не нулевой
    """
    return True if n % divisor == 0 else False


def decimal_to_binary(decimal):
    binary = ''
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2
    return binary


def binary_to_decimal(binary):
    decimal = 0
    for i in range(len(binary)):
        decimal += int(binary[i]) * (2 ** (len(binary) - 1 - i))
    return decimal


def remove_repetitions(lst):
    """
    Функция убирает дубликаты значений в списке

    :param lst: Список из которого необходимо убрать дублированные значения
    :return: Возвращается *упорядоченный* список уникальных значений
    """
    return list(set(lst))


def remove_repetitions_wos(lst):
    """
    Функция убирает дубликаты значений в списке, без последующей сортировки

    :param lst: Список из которого необходимо убрать дублированные значения
    :return: Возвращается список уникальных значений
    """
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result


def count_sum_of_digits(n: [float, int, str]):
    """
    Функция подсчитывает сумму цифр из которых состоит переданное ф-ции число
    Например: 56 -> 11, 23.5 -> 10

    :param n: Число, сумму цифр которого нужно подсчитать, могут быть переданы типы данных int, float, str
    :return: Сумма цифр из которых состоит число n
    """
    n = str(n).replace('.', '').replace(',', '')
    try:
        if isinstance(int(n), int):
            return sum([int(digit) for digit in n])
    except ValueError:
        print(f'{n}, не соответствует входным параметрам функции!')


