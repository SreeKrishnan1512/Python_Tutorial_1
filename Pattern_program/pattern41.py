n=4
current_number=0
for i in range(1,2*n):
    
    if (i<=n):
        j=(i+2)

    else:
        j= i-current_number
        current_number=current_number+2

    print(str(j)*(j-2))
        

   

 
