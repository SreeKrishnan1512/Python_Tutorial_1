def EvenorOdd(a):
    if(a%2==0):
        return True
    
    else:
        return False
    


a=int(input("Enter the number: "))

b=EvenorOdd(a)

def Return():
    print(f"The given number is even- {b}")

Return()