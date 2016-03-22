n = int(raw_input())

def Staircase(n):
    for i in range(1, n + 1):
        print (n - i) * ' ' + i * '#'

if __name__ == '__main__':
    Staircase(n)

