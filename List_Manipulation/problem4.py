n=int(input("Enter the number: "))

c=[]

for i in range(1,n+1):

    a=int(input(f"Enter the value {i}: "))

    c.append(a)

print(c)

c.remove(1)

print(c)