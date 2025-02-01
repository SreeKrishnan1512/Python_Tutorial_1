count=0
for i in range(1,6):
    for j in range(1+count,i+1+count):
        print(j, end=" ")
        count=count+1
    print("\n")
    