# Self keyword is important for calling instance variable into the method
# instance and class variable have whole different purpose
# Constructor name should be __init__
# new keyword is not required when you create object

class Calculator:

    num=100

    def __init__(self,a,b):
        self.FirstNumber=a
        self.SecondNumber=b
    
    def Addition(self):

        return (self.FirstNumber+self.SecondNumber+self.num)
    

    



#obj=Calculator(2,3)

#print(obj.Addition())
