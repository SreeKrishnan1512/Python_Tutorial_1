
n=5
count=4
for i in range(0,n):
    k=1
    for j in range(0, 5):
        if (i+j)>=(n-1):
            print(k,end=' ')
            k=k+1
        else:
            print("-",end=' ')
    print("\n")