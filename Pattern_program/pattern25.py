for i in range(1,4+1):

    for j in range(1,4-i+2):
        c=chr(64+j)
        print(c,end=" ")

    for j in range(1,(2*i)-2+1):
        print("-",end=" ")

    for j in range(1,4-i+2):
        c=chr(69-j)
        print(c,end=" ")


   
    

    print("\n")