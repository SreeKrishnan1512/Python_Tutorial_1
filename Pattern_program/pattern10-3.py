for i in range(1,5+1):
    for j in range(1,5-i+1): #for dash
        print("-",end=" ")

    for j in range((2*i)-1):
        print("*",end=" ")

    for j in range(1,5-i+1): #for dash
        print("-",end=" ")
    
    print("\n")
    