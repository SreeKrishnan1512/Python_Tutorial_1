count=0

n=5
for i in range(1,5+1):
    current_number=i
    increment=n-1
    for j in range(1,i+1):
        
            
        if(j==1):
            print(i,end=" ")
            count=count+1
           
        else:
           
            current_number=current_number+increment
            print(current_number,end=" ")
            increment=increment-1
            

           
            
        
            

            
        #count1=count1+1
        
    print("\n")
    