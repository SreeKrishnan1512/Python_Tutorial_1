for i in range(1,9+1):
    if(i==1 or i ==9):
        star= "* " * 9
        print(star,end=" ")
    else:
        star="* "
        empty="  " * 7
        result= star+empty+star
        print(result,end=" ")
    print("\n")
    
   

