start=1
end=20
for i in range(start,end+1):
    for j in range(start,end+1):
        if(i== start or i ==end):
          print("*",end=" ")
        else:
           if(j==start or j==end):
              print("*",end=" ")
           else:
            print(" ",end=" ")
           
    print("\n")