a=[1,0,2,0,3,4,5]

b=[i for i in a if i!=0] + [i for i in a if i==0]

print(b)