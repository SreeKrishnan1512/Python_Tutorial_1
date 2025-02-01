f1=open("file1.txt","r")

content=f1.readlines()

a=[]
b=[]
count=0

for i in content:

    c=i.split()
    a.append(c)

for i in a:
    b.extend(i)

print(b)

for i in b:

    for j in i:
        if  any(c.isupper() for c in j):
            count=count+1
            print(j,end=" ")
    
print("\n")

print(count)
