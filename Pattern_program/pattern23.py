
n=int(input("Enter the number"))
for i in range(1, n+1):
    count=0
    
    for j in range(n,n-n+i-1,-1):
        print(" ",end=" ")

    for j in range(i,i+i):
        print(j,end=" ")

    for j in range(1,i-1+1):
        k=(2*i)-2
        print(k-count,end=" ")
        count=count+1
         
    for j in range(n,n-n+i-1,-1):
        print(" ",end=" ")

    print("\n")
        
