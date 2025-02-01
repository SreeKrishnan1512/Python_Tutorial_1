count1=0

for i in range(1,5+1):
    num=i
    decr= 5-1

    for j in range(1,i+1):
        
        if(j==1):
            print(i,end=" ")
        
        else:
            num=num+decr
            print(num,end=" ")
            decr=decr-1
    print("\n")
