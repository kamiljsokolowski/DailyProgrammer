# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.

#1
# go by each number from 1 to 999 and check if rest from division by 3/5 is 0
# if it is add the number to sum

#2
# start from 3, for each iteration add 3 and sum until the number is equal 999
# start from 5, fro each iteration add 5 and sum until the number is equal 999
# common function
def add_check(base,multiply,sum3):
    while base < 34:
        print "base = %d" % base
        print "sum = %d" % sum3
        sum3 += base
        base += multiply
    return sum3

print add_check(3,3,0)
