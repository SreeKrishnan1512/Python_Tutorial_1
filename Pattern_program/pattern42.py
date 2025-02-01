for i in range(1,4+1):

    for j in range(1,((2*i)-1)+1):

        if (j%2==0):
            print("*",end=" ")

        else:
            print(i,end=" ")

    print("\n")

for i in range(4,0,-1):

    for j in range(1,((2*i)-1)+1):
        if (j%2==0):
            print("*",end=" ")

        else:
            print(i,end=" ")

    print("\n")
