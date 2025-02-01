a= int(input("Enter the Number"))
temp =a
sum=0
while(temp>0):
    rem=temp%10
    sum= sum+(rem**3)
    temp=temp//10


if(sum == a):
    print("The number", a, "is an Armstrong number")

else:
    print("The number", a, "is not an Armstrong number")


