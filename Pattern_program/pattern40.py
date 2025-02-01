for i in range(1,7+1):
    for j in range(1,7+1):

        if (i==1 or i==7 or j==1 or j==7):
            print("*",end=" ")

        elif(j==i or j==7-i+1):
            print("*",end=" ")

        else:
            print(" ",end=" ")

    print("\n")