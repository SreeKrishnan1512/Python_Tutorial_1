f1=open("file1.txt","r")
f2=open("file2.txt","w")

content= f1.readlines()

a=[]
b=[]


for i in content:
    s1=""
    s2=""
    c=i.split()

    for j in i:

        if j.isalpha():
            s1=s1+j

        else:
            s2=s2+j
        
    a.append(s1)
    b.append(s2)

print(a)

print(b)


d=[]

for i in range(0,len(a)):

    c=a[i]+" "+b[i]
    d.append(c)

print(d)

f2.writelines(d)



