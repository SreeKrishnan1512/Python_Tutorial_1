class Calculator:

    def __init__(self):
        print("I am called automatically without being called")

    def addi(self):
        return ("My function is to add")
        


obj= Calculator()
Add=obj.addi()
print(Add)