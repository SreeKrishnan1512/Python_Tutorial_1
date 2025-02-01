a=[6,0,1,3]
b=[4,7,4,2]
max=0
c=""

if (len(a))>(len(b)):

    max=len(a)

else:
    max=len(b)

count=(max-1)
for i in range(0,4):

    if count!=0:
        d=a[i]+b[i]
        
        f=f"{d} X^{count} + "
        c=c+f
        count=count-1
    else:
        d=str(a[i]+b[i])
       
        c=c+d
print(c)






