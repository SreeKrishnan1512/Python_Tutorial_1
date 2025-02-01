import random
def Random(n):
    if n==1:
        c=random.randint(0,9)
        print(c)
    elif n==2:
        c=random.randint(10,99)
        print(c)
    else:
        c=random.randint(100,999)
        print(c)

Random(3)
    