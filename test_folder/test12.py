for i in range(0,7+1):
    count=0
    for j in range(0,(2*i)+1):

        if j==0 or i==0 or j==(2*i):
            print("*",end=" ")
        else:
            count=count+1
            print(count,end=" ")
        
    print("\n")