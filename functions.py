def get_prime_factors(n: int):
    """
    Функция для нахождения натуральных множителей числа n.
    Пример: 8 -> 2 * 2 * 2

    :param n: Число, натуральные множители которого необходимо найти.
    :return: Возвращает список натуральных множителей числа n.
    """
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
    """
    Функция для проверки является ли число n натуральным.
    Пример: 5 -> True

    :param n: Число, которое будет проверено, является ли оно натуральным.
    :return: Возвращает True - если натуральное или False - если нет.
    """
    return isinstance(n, int) and n >= 1


def check_remainder(n, divisor):
    """
    Проверка остатка от деления, например, проверка четности, как частный случай, это check_remainder(4, 2) -> True

    :param n: Число остаток от деления которого будим проверять
    :param divisor: Делитель числа n
    :return: True - если остаток от деления равен нулю или
            False - если остаток от деления не нулевой
    """
    return True if n % divisor == 0 else False


def decimal_to_binary(n) -> str:
    """
    Функция для перевода числа n из десятичной системы исчисления в двоичную.
    Пример 51 -> 110011

    :param n: Число в десятичной системе исчисления.
    :return: Возвращается число в бинарной системе исчисления, в виде строки.
    """
    binary = ''
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    return binary


def binary_to_decimal(n: str) -> int:
    """
    Функция для перевода числа n из бинарной системы исчисления в десятичную.
    Пример 110011 -> 51

    :param n: Число в двоичной системе исчисления в виде строки(str).
    :return: Возвращается число в десятичной системе исчисления.
    """
    decimal = 0
    for i in range(len(n)):
        decimal += int(n[i]) * (2 ** (len(n) - 1 - i))
    return decimal


def remove_repetitions(n):
    """
    Функция убирает дубликаты значений в списке
    Пример [6, 2, 3, 2, 5, 2] -> [2, 3, 5, 6]

    :param n: Список из которого необходимо убрать дублированные значения
    :return: Возвращается *упорядоченный* список уникальных значений
    """
    return list(set(n))


def remove_repetitions_wos(n):
    """
    Функция убирает дубликаты значений в списке, без последующей сортировки
    Пример [6, 2, 3, 2, 5, 2] -> [6, 2, 3, 5]

    :param n: Список из которого необходимо убрать дублированные значения
    :return: Возвращается список уникальных значений
    """
    result = []
    for item in n:
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


def get_distance(v1, v2):
    """
    Фунция для нахождения расстояния между двумя точками в многомерных пространствах.
    Пример: [0,0,4], [3,0,0] -> 5.0

    :param v1: Список или коржет из координат первой точки.
    :param v2: Список или коржет из координат второй точки.
    :return: Возвращает расстояние между двумя точками.
    """
    sum_of_squares = 0
    if len(v1) == len(v2):
        for i in range(len(v1)):
            sum_of_squares += (v1[i] - v2[i]) ** 2
        return sum_of_squares ** 0.5
    else:
        return False
