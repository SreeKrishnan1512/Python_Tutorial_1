n1=int(input("Enter Number 1: "))
n2=int(input("Enter Number 2: "))
c=[]

for i in range(n1,n2):
    if(i%2!=0):
        c.append(i)

print(c)