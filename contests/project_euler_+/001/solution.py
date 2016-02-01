def sum_multiples_of_three_and_five(number):
    sum_3 = (3 + ((number - 1) // 3) * 3)
    sum_3 *= (number - 1) // 3
    sum_3 /= 2
    sum_5 = (5 + ((number - 1) // 5) * 5)
    sum_5 *= (number - 1) // 5
    sum_5 /= 2
    sum_15 = (15 + ((number - 1) // 15) * 15)
    sum_15 *= (number - 1) // 15
    sum_15 /= 2

    total = sum_3 + sum_5 - sum_15

    return total


def main():
    n_cases = int(raw_input())
    for i in xrange(n_cases):
        case = int(raw_input())
        print "{0}".format(sum_multiples_of_three_and_five(case))
    return 0

if __name__ == "__main__":
    main()
