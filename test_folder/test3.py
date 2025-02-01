a="python"
n=len(a)

for i in range((n+1)//2):
    for j in range(n):
        if ( j==i or j==6-i-1):
           
           print(a[j]+" ",end=" ")
        else:
            print(" ",end=" ")

    print()
           





