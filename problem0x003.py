# python 3
# (C) Simon Gawlik
# started 8/1/2015


n = 600851475143
max_factor = 0
max_prime_factor = 0

def isPrime (factor):
    for i in range (2, factor):     # use sqrt
        if factor % i == 0:
            return (max_prime_factor)
    print ("prime factor: " + str(factor))
    # n = n / factor
    return (factor)
    

for counter in range (2, n):        # divide last number by 2
    if n % counter == 0:
        max_factor = counter
        tmp = max_prime_factor
        max_prime_factor = isPrime (max_factor)
        if tmp != max_prime_factor:
            n = n // max_prime_factor
            if n == 1:
                break
         
print ("Largest Prime Factor: " + str(max_prime_factor))
