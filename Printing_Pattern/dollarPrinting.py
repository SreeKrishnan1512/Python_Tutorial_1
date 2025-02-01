start=1
end=6
for i in range(start, end):
    for j in range(start,end):
        if(i==j or i+j==end):
              print("+",end= " ")
        
        else:
              print("-", end=" ")
        
    print("\n")