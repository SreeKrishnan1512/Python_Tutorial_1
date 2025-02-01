def NumberType(a):
    if (a>0):
        print(f"{a} is Positive number")

    elif(a<0):
        print(f"{a} is a Negative number")

    else:
        print(f"{a} is Zero")


a=int(input("Enter the number: "))
NumberType(a)