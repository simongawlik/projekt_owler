# python 3
# (C) Simon Gawlik
# started 8/1/2015


# number of digits for multipliers. question asks for product of two 3-digit 
# factors
digits = 3

# lowest and highest possible product of two numbers for given # of digits
upper_bound = (10 ** digits - 1) ** 2
lower_bound = (10 ** (digits - 1)) ** 2

# lowest and highest possible factors for given # of digits
lo_digit = 10 ** (digits - 1)
hi_digit = (10 ** digits) - 1

#print ("upper bound: " + str(upper_bound))
#print ("lower bound: " + str(lower_bound))


# turn number into an array
def array_of_number (y):
    a = []
    while y >= 1:

        a.append(y % 10)
        y = y // 10
    return (a)

assert array_of_number(198001) == [1, 0, 0, 8, 9, 1]


# compare corresponding digits to each other
def is_palindrome (z):
    array_len = len(z)
    for counter in range (0, array_len // 2 + 1):   # no need to check twice
        if z[counter] != z[array_len - counter - 1]:
            return (False)
    return (True)

assert is_palindrome(array_of_number(91019)) == True
assert is_palindrome(array_of_number(81019)) == False
assert is_palindrome(array_of_number(1001)) == True
assert is_palindrome(array_of_number(123101321)) == True
assert is_palindrome(array_of_number(81019123)) == False


# check if palindrome has factors with same number of digits
def factor_magnitudes_same (palindrome):
    for counter in range (lo_digit, hi_digit):
        if (palindrome % counter == 0 and 
            palindrome / counter >= lo_digit and 
            palindrome / counter <= hi_digit):
            #success
            return (True)
            break
    return (False)


# main function
for counter in range (upper_bound, lower_bound, -1):
    if is_palindrome(array_of_number(counter)):        
        if factor_magnitudes_same (counter):
            print(str(counter))
            break
