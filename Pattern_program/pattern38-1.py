count=0
for i in range(5,0,-1):
    for j in range(1,9+1):  
        if j==i or j== 5+count :
           print("*",end=" ")

       

        elif (i==1 or j==5):
            print("*",end=" ")

        else:
            print(" ",end=" ")
    count=count+1
    print("\n")



    