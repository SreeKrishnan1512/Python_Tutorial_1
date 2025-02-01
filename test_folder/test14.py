a=[1,0,2,0,3,4,5]
b=[]
c=[]

for i in range(0,len(a)):
    if a[i]!=0:
        b.append(a[i])
    else:
        c.append(a[i])
    

b.extend(c)
print(b)

