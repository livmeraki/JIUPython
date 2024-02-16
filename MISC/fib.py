import random as rand


tree = 0
forest = 10
fib = [0,1,1,2,3,5,8,13,21,34]

for i in fib:
    if len(str(i))>1:
        length_of_sample = 2 # <- Also known as n
        samp = rand.sample(fib, length_of_sample)
        print(i, end='')
    else:
        continue
    print("-", end='')
    
    
