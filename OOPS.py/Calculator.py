class Calculator:

    def __init__(self,a,b):
        self.a=a
        self.b=b
    
    def Addition(self):
        return(f"The addition of {self.a} and {self.b} is {self.a + self.b}")

    def Subtraction(self):
        return(f"The Subtraction of {self.a} and {self.b} is {self.a - self.b}")
    
    def Multiplication(self):
        return(f"The Multiplication of {self.a} and {self.b} is {self.a * self.b}")
    
    def Division(self):
        return(f"The division of {self.a} and {self.b} is {self.a // self.b}")

result=[]
       

a=int(input("Enter the number: "))
b=int(input("Enter the number: "))

calculator= Calculator(a,b)

result.append(calculator.Addition())

print(result)

