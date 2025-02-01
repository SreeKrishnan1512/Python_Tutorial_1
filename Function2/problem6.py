def footToInch(foot):
  inch=12*foot
  return inch

n=int(input("Enter the value in foot: "))
a=footToInch(n)

def Return():
    print(f"The foot '{n}' is converted to inch and its value is '{a}' ")

Return()

def InchtoFeet(Inch):
   
    Feet=Inch/12
    print(f"The Inch '{Inch}' is converted to feet and its value is {Feet}")

Inch= int(input("Enter the value for Inch: "))

InchtoFeet(Inch)

