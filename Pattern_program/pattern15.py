for i in range(1,9+1):
    if(i==1 or i==9):
         for j in range(1,9+1):
            print("* ",end=" ")
    
    else:
        for j in range(1,9+1):
            if(j==1 or j==9):
                star="* "
                print(star,end=" ")
            else:
                if(i==j):
                  print("* ",end=" ")

                else:
                    print("  ",end=" ")

        

            
    print("\n")
