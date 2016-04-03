import sys

def is_positive(matrix, reverse=False):
    """ Return number of positive, negative and zero array elements. """
    pos, neg, zero = 0, 0, 0
    for i in arr:
        if i > 0:
            pos += 1
        elif i < 0:
            neg += 1
        else:
            zero += 1
    return pos, neg, zero

if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    arr = map(int, sys.stdin.readline().strip().split(' ')) 

    for i in is_positive(arr):
        print round(i / float(n), 6) 
