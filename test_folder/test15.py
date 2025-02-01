a=[1,2,0,4,0,5,6]
b=[]

for i in a:
    if i!=0:
        b.append(i)

b=b+ [0] * a.count(0)

print(b)
    

