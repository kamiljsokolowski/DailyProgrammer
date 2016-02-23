def is_palindrome(s):
    if s == s[::-1]:
        return True
    return False

if __name__ == '__main__':
    for n1 in range(100,1000):
        for n2 in range(100,1000):
            m = n1 * n2
            if is_palindrome(str(m)):
                print m

