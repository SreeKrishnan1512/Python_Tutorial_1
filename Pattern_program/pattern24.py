
n=int(input("Enter the Number: "))

count3=0
count1=0 # for  if(i%2!=0):
for i in range(1, n+1):
    count=1 # for if(i%2!=0):
    count2=0

    if(i%2!=0):
        for j in range(n-i+1,0,-1):
            print(n-n+count+count1,end=" ")
            count=count+1

        count1=count1+1

    else:
        for j in range(i,n+1):
            print(((i+(n-i))- count2-count3),end=" ")
            

            count2=count2+1
        count3=count3+1




    print("\n")
          