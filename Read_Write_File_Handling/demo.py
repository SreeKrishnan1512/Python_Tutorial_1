f=open("demo.txt","r")
content=f.readlines()
a=" "



f1=open("demo2.txt","w")

for i in content:
    
    a=a+i

c=a.split()
print(c)



for i in c:

    if i!="The":
        
        print(i+" ",end=" ")
    
    else:
        print("That"+" ",end=" ")
    
    f1.write(i+" "+"\n")
    











f.close()

