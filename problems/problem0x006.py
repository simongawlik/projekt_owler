# python 3
# (C) Simon Gawlik
# started 8/2/2015

# Almost OCaml, baby!
import functools


n = 100

# sum of squares
squares = list(map(lambda x: x**2, range(1, n + 1)))
print (squares)
sum_of_squares = functools.reduce(lambda x, y: x + y, squares)

# square of sum
sum = functools.reduce(lambda x, y: x + y, range (1, n + 1))
print (sum)
square_of_sum = sum ** 2

#result
print (square_of_sum - sum_of_squares)
