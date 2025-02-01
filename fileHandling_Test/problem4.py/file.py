f1=open("file1.txt","r")

content=f1.readlines()
d=[]
e=[]

count_to=0
count_the=0

for i in content:

    c=i.split()
    d.append(c)

for i in d:
    e.extend(i)

print(e)

for i in e:

    if i =="to":
        count_to+=1
    elif i =="the":
        count_the+=1

print(count_to)
print(count_the)

f1.close()



