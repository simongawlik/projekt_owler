# python 3
# (C) Simon Gawlik
# started 8/1/2015


f1 = 1
f2 = 2

tmp = 0
sum = 0

# sum fib numbers
while f2 < 4000000:
    tmp = f1
    f1 = f2
    f2 = f2 + tmp
    if f1 % 2 == 0:
        sum = sum + f1

print ("Sum: " + str(sum))
