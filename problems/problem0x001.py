# python 3
# (C) Simon Gawlik
# started 8/1/2015

n = 13195
sum = 0

for counter in range (1, n):
    if counter % 3 == 0 or counter % 5 == 0:
        sum = sum + counter
    
print ("Sum: " + str(sum))
