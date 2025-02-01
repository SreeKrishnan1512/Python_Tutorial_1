for i in range(1,6+1):
    
        if(i ==1):
            star= "* " * 9
            print(star,end=" ")


        else:
          
            star="* " * (5-i+1)
            empty= "  " * ((2*i)-3)
            result= star+empty+star
            print(result,end=" ")
          

        print("\n") 