from itertools import zip_longest
a=[1,6,4,8,5]
b=[4,6,4,7]
c=[]

for index,(coeff_a,coeff_b) in enumerate(zip_longest(a,b,fillvalue=0)):
    d=coeff_a+coeff_b
    c.append(d)

print(c)
