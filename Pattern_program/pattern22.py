count=0
char_count=1
for i in range(1,5+1):

    for j in range(1+count,i+1+count):
        
        if(i%2!=0):
            print(j,end=" ")
            
            count=count+1

        else:
            print(chr(64+char_count),end=" ")
            char_count=char_count+1
            
                

    print("\n")
   

       