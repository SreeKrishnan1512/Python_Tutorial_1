def Divisible(a,b):
    if (a%b==0):
        print(f"{a} is divisible by {b}")

    else:
        print(f"{a} is not divisible by {b}")


a=int(input("Enter the number: "))
b=int(input("Enter the number: "))

Divisible(a,b)