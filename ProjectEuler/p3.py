def find_prime_factors(n):
    i = 2
    while i * i < n:
        while n % i == 0:
            n = n / i
        i += 1
    return n

if __name__ == '__main__':
    test = [13195, 600851475143]
    for n in test:
        print find_prime_factors(n)

