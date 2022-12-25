import school_functions as sf


@sf.execution_time
def main():
    print(sf.binary_to_decimal('110011'))
    print(sf.get_prime_factors(225))
    print(sf.is_natural(5.2))
    print(sf.check_remainder(9, 3))
    print(sf.decimal_to_binary(5))
    print(sf.remove_repetitions([2, 2, 5, 3]))
    print(sf.remove_repetitions_wos([2, 2, 5, 3]))
    print(sf.count_sum_of_digits('24.5'))
    print(sf.get_distance([0, 4, 0], [3, 0, 0]))


if __name__ == '__main__':
    main()
