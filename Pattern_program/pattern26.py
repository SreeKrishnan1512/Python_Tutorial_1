for i in range(1,5+1):

    if(i%2!=0):
       
            And="& " *i
            Hash="# " *(9-i)
            result=And+Hash
            print(result,end="  ")

    if(i%2 ==0):
        
            Hash="# " * (9-i)
            And= "& " * i
            result= Hash+And
            print(result,end="  ")

    print("\n")


for i in range(4,0,-1):

    if(i%2==0):
        
          Hash= "# " *(9-i)
          And= "& " *(i)

          result= Hash+And
          print(result,end="  ")

    if (i%2!=0):
          
          And= "& " *i
          Hash= "# " *(9-i)

          result= And+Hash
          print(result,end="  ")



           
        
    


           
        
    print("\n")



