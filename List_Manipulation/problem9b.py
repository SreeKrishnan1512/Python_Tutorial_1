a=[]
n=5

for i in range(1,n+1):

    num= int(input("Enter the number: "))

    a.append(num)



print(a)

for i in range(0,n):

    a[i]=a[i]+5

print(a)


