for i in range(1,5+1):
    for j in range(1,5-i+1):
        print("-",end=" ")
    for j in range(i):
        print("*",end=" ")
    print("\n")