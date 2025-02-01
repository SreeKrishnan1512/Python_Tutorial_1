n=int(input("enter the number: "))
for i in range(1,((n//2)+1)):
 
 if i<=9:
    
    for j in range(1,i+1):
            
        number= (i+i)-1
        print(" ",number,end="  ")
        

    for j in range(1,(n-(2*i))+1):
        print("- ",end=" ")

    for j in range(1,i+1):
            
        number= (i+i)-1
        print(" ",number,end="  ")

 else:
    for j in range(1,i+1):
            
        number= (i+i)-1
        print(number,end="  ")
        

    for j in range(1,(n-(2*i))+1):
        print("- ",end=" ")

    for j in range(1,i+1):
            
        number= (i+i)-1
        print(number,end="  ")
        
      
    
 print("\n")