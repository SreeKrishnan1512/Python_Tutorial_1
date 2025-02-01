a=[1,2,0,0,3,0,4,5]
b=[]
count_zero=0

for i in a:
    if i!=0:
        b.append(i)
    else:
        count_zero+=1

b=b+ [0] * count_zero

print(b)