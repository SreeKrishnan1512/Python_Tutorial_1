f=open("demo.txt","r")

content=f.readlines()

f1=open("demo2.txt","w")

for i in content:
    updated= i.replace("The","That")
    f1.write(updated)




f.close()
f1.close()

