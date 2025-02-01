for i in range(1,5+1):
    if i ==1 :
      print("* " * 9, end=" ")
    else:
       empty= "  " * (i-1)
       star= "* " * (7-((i-2)*2))
       result= empty+star+empty
       print(result,end=" ")
    
    print("\n")
   
for i in range(1,4+1):
    if i==4:
       print("* " *9,end=" ")
    else:
       empty= "  " *(3-(i-1))
       star= "* " * ((2*i)+1)

       result= empty+star+empty
       print(result,end=" ")

    print("\n")
   