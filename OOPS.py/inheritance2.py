from MainConstructor import Calculator

class Child_Implement(Calculator):

    num3=100

    def __init__(self, a, b):
        super().__init__(a, b)

    def Summation(self):
        add= self.Addition()
        return (self.num+self.num3+add)
    
    def Return_Check(self):
        c=self.Summation()
        return c

    def Return_Check2(self):
        print(self.Return_Check())
    
    
Child_Implement_Obj= Child_Implement(2,3)

print(Child_Implement_Obj.Summation())
Child_Implement_Obj.Return_Check2()

#Return will be shown only when it is printed
