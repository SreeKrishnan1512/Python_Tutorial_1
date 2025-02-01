a=int(input("enter the number"))
temp=a
b=[]
while(temp>0):
    r=temp%2
    c=str(r)
    b.append(c)
    temp=temp//2

b.reverse()
print(b)

singleString= ''.join(b)
print(singleString)



    



