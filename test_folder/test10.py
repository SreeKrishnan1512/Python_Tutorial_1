n= str(input("Enter the number: "))

print(n)

a=[]

for i in n :

    b=int(i)
    c=b **3
    a.append(c)

print(a)

count=0

for i in a:

    count=count+i

print(count)

int_n = int(n)

if int_n == count:

    print(f"{n} is an armstrong number")

else:
        print(f"{n} is not an armstrong number")







    

