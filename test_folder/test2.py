a=int(input("enter the number: "))
b=[]
c=[]

for i in range(1,a+1):
    x=int(input(f"enter the number {i}: "))
    b.append(x)
    

print(b)

for i in b:
    if(i%2 !=0):
        c.append(i)

print(c)

c.sort()
print(c)

c.reverse()
print(c)
print(f" the maximum number is {c[0]}")



   
        
        
