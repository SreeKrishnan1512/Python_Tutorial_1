current_Number=0

count_first_i=1
count_last_i=10
count_first_j=1
count_last_j=10


matrix= [[0] * 10 for _ in range(10)]




'''

for i in range(count_first_i,count_last_i+1):

    for j in range(count_first_j,count_last_j+1):

        if i==count_first_i:
            current_Number=current_Number+1
            print(current_Number,end=" ")
        count_first_i=count_first_i+1
        
        if j==count_last_j:
            current_Number=current_Number+1
            print(current_Number,end=" ")
        count_last_j=count_last_j-1

        if i== count_last_i:
            for k in range(count_last_j,count_first_j-1,-1):
                current_Number=current_Number+1
                print(current_Number,end=" ")
        count_last_i=count_last_i-1

        if j==count_first_j:
            for k in range(count_last_i,count_first_i-1,-1):
                current_Number=current_Number+1
                print(current_Number,end=" ")
        count_first_j=count_first_j+1

        
    
    print("\n")

'''
        
            
            


