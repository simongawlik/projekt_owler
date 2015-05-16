# python 3
# (C) Simon Gawlik
# started 8/1/2015

n = 20          #232792560
primes = []
non_primes = []

# find prime numbers up to n
def primes_lt_n (n):
    for num in range (2, n + 1):
        is_prime = True
        for i in range (2, num):
            if num % i == 0:
                is_prime = False
        if is_prime:
            primes.append(num)
        else:
            non_primes.append(num)

primes_lt_n (n)
#print (primes)
#print (non_primes)

# find the product of all the positive integers smaller than or equal to number
def get_max_product (number):
    if number <= 2:
        return (number)
    else:
        max_product = 1
        for counter in range (1, number + 1):
            max_product = max_product * counter
        return (max_product)

# tests
assert get_max_product (0) == 0
assert get_max_product (1) == 1
assert get_max_product (2) == 2
assert get_max_product (3) == 6
assert get_max_product (10) == 3628800
assert get_max_product (11) == 39916800

max_product_n = get_max_product (n)

# check if a number is divisible by all the numbers in a given list
def has_divisors_in (number, lst):
    for member in lst:
        if number % member != 0:
            return (False)
            break
    return (True)

# main
for counter in range (n, max_product_n):
    if (has_divisors_in (counter, primes) and       # check for primes first
        has_divisors_in (counter, non_primes)):
        print (counter)
        break
    

