import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

def sum_elements(arr):
    """ Return sum of array elements. """
    return sum(arr)

if __name__ == '__main__':
    print sum_elements(arr)

