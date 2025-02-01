def Minimum_oneDigit(a,b):

    c=a%10
    d=b%10

    if (c < d):
        print(f"{d}'s one digit of number {b} is greater")
    
    elif(c>d):
        print(f"{c}'s one digit of number {a} is greater")

    else:
        print(f"Equal one digit number")

a=int(input("Enter the number: "))
b=int(input("Enter the number: "))

Minimum_oneDigit(a,b)



