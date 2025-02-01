f1=open("file1.txt","r")

content=f1.readlines()

print(content)


f2=open("file2.txt","w")

for i in content:
    c=i.split()
    
    #print(c)
    for j in c:

        print(j,end=" ")
        f2.write(j+" ")
    

    f2.write("\n")
    
    


        



    
        










