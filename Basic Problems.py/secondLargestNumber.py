a=int(input("enter a number: "))
b=int(input("enter a number: "))
c=int(input("enter a number: "))

d=[a,b,c]
e=d
e.sort(reverse= True)
print(e)

f=e[1]
print("The second largest number is", f)