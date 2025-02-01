
for i in range(0,4):
    count=0
    for j in range(0,(2*i)+1):
      
        if j==0 or j == (2*i) :
            print("*",end=" ")

        else:
            if j<=i:
                count=count+1
                print(count,end=" ")
                
            elif j>i:
                count=count-1
                print(count,end=" ")


    print("\n")

        



