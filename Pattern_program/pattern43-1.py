c=7
a=c

for i in range(4,0,-1):

    d=a-i

    for j in range(1,2*i):

        if j%2!=0:
            print(c,end=" ")

            c=c+1

        else:
            print("*",end=" ")

    c=d+1
    a=c
    print("\n")