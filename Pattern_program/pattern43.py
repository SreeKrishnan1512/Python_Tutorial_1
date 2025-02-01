count=0
for i in range(1,4+1):
   
    for j in range(1,((2*i)-1)+1):

        if (j%2==0):
            print("*",end=" ")

        else:
            count=count+1
            print(count,end=" ")

    print("\n")



a=6
current_num=a

for i in range(4,0,-1):
    
   
    for j in range(1,((2*i)-1)+1):
    
        if (j%2==0):
            print("*",end=" ")

        else:
            current_num=current_num+1
            print(current_num,end=" ")
            #current_num=current_num+1
    current_num=a-i+1
    a=current_num
            

    print("\n")

