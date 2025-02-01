f1=open("file1.txt","r")

content=f1.readlines()

a=[]
b=[]

for i in content:

    c=i.split()
    a.append(c)

for i in a:
    b.extend(i)

print(b)

for i in b:
    if  i[0].isupper():
        print(i,end=" ")
