for i in range(1,5+1):
    for j in range(1,9+1):
        if(i==5):
            print("* ",end=" ")

        elif (j==5+i-1):
            print("* ",end=" ")

        else:
            print("  ",end=" ")

    print("\n")

for i in range(2,5+1):
    for j in range(1,9+1):
        if (j==10-i):
            print("* ",end=" ")
        else:
            print("  ",end=" ")

    print("\n")