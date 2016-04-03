import sys

def print_staircase(n):
    """ Print a staircase of n hight. """
    for i in range(1, n + 1):
        print (n - i) * ' ' + i * '#'


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())

    print_staircase(n)
