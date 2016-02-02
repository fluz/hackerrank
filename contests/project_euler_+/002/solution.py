def sum_even_fib(n):
    sumfib = 0
    a, b = 0, 1
    while b < n:
        if b % 2 == 0:
            sumfib = sumfib + b
        a, b = b, a + b
    return sumfib


def main():
    nTest = int(raw_input())
    for i in xrange(nTest):
        limit = int(raw_input())
        print "{0}".format(sum_even_fib(limit))

if __name__ == "__main__":
    main()
