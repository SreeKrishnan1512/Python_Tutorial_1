n=int(input("enter the number"))

c=[]
d=[]

for i in range(2,n):
    if (n%i ==0):
        c.append(i)
        
print(c)
for i in c:
    count=0
    
    for j in range(1,i):
        if(i%j==0):
         count=count+1
    if(count==1):
       d.append(i)
print(d)
