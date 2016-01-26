def gen_fibonacci(start, stop):
    """
    Create a list of Fibonacci numbers.
    Start with list of 2 elements and stop, when the last number' value is equal or exceeds stop.
    """
    fib = start
    i = 1
    n = 0
    while True:
        n = fib[i] + fib[i - 1]
        if n >= stop:
            break
        fib.append(n)
        i += 1
    return fib


def sum_even(l):
    """
    Return a sum of all even elements of a list.
    """
    sum = 0
    i = 0
    for i in range(len(l)-1):
        if l[i] % 2 == 0:
            print l[i]
            sum = sum + l[i]
    return sum


if __name__ == '__main__':
    print gen_fibonacci([1, 2], 4000000)
    print sum_even(gen_fibonacci([1, 2], 4000000))

