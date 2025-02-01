w= "Spider-man"

def Spidy():
   global w
   w="Batman"

print("I am",w)
Spidy()
print("I am",w)

print("End of first function")
print()

#############################################################################
x="python" #this x is a global variable
def myfunc():
   
   x= "c++" #this x is a local variable
   print(x,"is awesome")

myfunc()
print (x, "is awesome")

print("End of Second function")
print()
#########################################################################

def secondfunc():
   global y 
   y= "Blockchain"


secondfunc()
print("I am a ", y, "developer")

print("End of Third function")
print()
##########################################################################

z= "Hello"
def thirdfunc():
   global z
   z="Good Bye"

thirdfunc()
print(z)

print("End of fourth function")
print()


