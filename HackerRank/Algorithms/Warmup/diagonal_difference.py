import sys

def diagonal(matrix, reverse=False):
    """ Return matrix' diagonal (count from the the back if reverse = True). """
    diag = 0
    if not reverse:
        for i in range(len(matrix)):
            diag += matrix[i][i]
    else:
        for i in range(len(matrix)):
            diag += matrix[i][(len(matrix) - 1) - i] 
    return diag


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    a = []

    for i in xrange(n):
       a_tmp = map(int, sys.stdin.readline().strip().split(' ')) 
       a.append(a_tmp)

    print abs(diagonal(a) - diagonal(a, True))
