import sys

def sum_elements(arr):
    """ Return sum of array elements. """
    return sum(arr)


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    arr = map(int, sys.stdin.readline().strip().split(' '))

    print sum_elements(arr)

