
top,bottom= 0,9
left,right=0,9
current_Number=0


matrix= [[0] * 10 for _ in range(10)]
#print(matrix)

while (bottom>=top and right>=left):

#from left to right
    for j in range(left,right+1):
        current_Number=current_Number+1
        matrix[top][j]=current_Number
        
    top=top+1

#from top to bottom
    for i in range(top,bottom+1):
        current_Number=current_Number+1
        matrix[i][right]=current_Number
        
    right=right-1   

#from right to left

    if (left<=right):
        for j in range(right,left-1,-1):
            current_Number=current_Number+1
            matrix[bottom][j]=current_Number

        bottom=bottom-1

    if (top<=bottom):

        for i in range(bottom,top-1,-1):
            current_Number=current_Number+1
            matrix[i][left]=current_Number

        left=left+1

for row in matrix:
   print( " ".join(f"{x:3}" for x in row))






    
    
    
