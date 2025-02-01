for i in range(1,5+1):
    empty= "  "*(5-i)
    star= "* "*1
    minus= "- " * ((2*i)-2-1)
    if(i ==1):
        result= empty+""+star
    else:
     result=empty+star+minus+star
    print(result, end=" ")
    print("\n")

for i in range(4,0,-1):
   empty= "  " * (5-i)
   star= "* " * 1
   minus= "- " * ((2*i) -3)
   
   if(i>1):
      result=empty+star+minus+star+empty
   else:
      result= empty+""+star+empty


   print(result,end=" ")
   print("\n")
      