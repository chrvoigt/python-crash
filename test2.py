import random

iterable =  (str(random.normalvariate (10, 100)) for i in range (0,100))
for s in iterable:
    print (s)