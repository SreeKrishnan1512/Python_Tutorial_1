# from fileName import className
from MainConstructor import Calculator

#class className(Parent_ClassName)
class ChildImp(Calculator):

    num2=200

    def __init__(self,a,b):

        # If parent class doesn't have default constructor and consist of constructor,
        # then Parent_className.__init__(self, value of a, value of b)
        
        Calculator.__init__(self,a,b)

    def Summation(self):
        add=self.Addition() #o/p is 105
        print(self.num + self.num2 + add) #100+200+105= 405

Child_Obj= ChildImp(2,3)
Child_Obj.Summation()

    

