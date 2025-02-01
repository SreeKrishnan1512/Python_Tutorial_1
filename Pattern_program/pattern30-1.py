count=10
count1=18
count2=36
for i in range(1,10+1):

    for j in range(1,10+1):

        if (i==1):
           
            print(j,end="  ")
        

        elif(j==10):
            count=count+1
            print(count,end=" ")

        elif(i==10):
            
            print(i+count1,end=" ")
            count1=count1-1

        elif (j==1):
            print(count2,end="  ")
            count2=count2-1

        else:
            print("- ",end=" ")

    print("\n")

    