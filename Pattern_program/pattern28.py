for i in range(5,0,-1):
 
    
    for j in range(i-1,0,-1):
         print(" ",end=" ")

    for j in range(5-i+1,0,-1):
        print(chr(64+j),end=" ")

    for j in range(1,5-i+1):
        print(chr(65+j),end=" ")

    


    
    print("\n")
        
