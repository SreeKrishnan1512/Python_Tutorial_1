

for i in range(1,6+1):
    count=1
    for j in range(0,i):
        if (j==0 ):
            print(1,end=" ")
        else:
            count=count*(i-j)//j
            print(count,end=" ")
    print("\n")
