# python 3
# (C) Simon Gawlik
# started 8/2/2015

import math

nth_prime = 10001

n_counter = 2
prime_counter = 0            

# count the number of primes, break on nth
while (True):
    prime = True
    # only go up to the sqare root to speed up algorithm
    for i in range (2, math.floor(math.sqrt(n_counter)) + 1):
        if n_counter % i == 0:
            prime = False
    if prime:
        prime_counter = prime_counter + 1
        if prime_counter == nth_prime:
            print (prime_counter)
            print (n_counter)
            break
    n_counter = n_counter + 1
