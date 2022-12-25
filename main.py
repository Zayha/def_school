import functions


@functions.execution_time
def main():
    print(functions.binary_to_decimal('110011'))
    print(functions.get_prime_factors(225))
    print(functions.is_natural(5.2))
    print(functions.check_remainder(9, 3))
    print(functions.decimal_to_binary(5))
    print(functions.remove_repetitions([2, 2, 5, 3]))
    print(functions.remove_repetitions_wos([2, 2, 5, 3]))
    print(functions.count_sum_of_digits('24.5'))
    print(functions.get_distance([0, 4, 0], [3, 0, 0]))


if __name__ == '__main__':
    main()
