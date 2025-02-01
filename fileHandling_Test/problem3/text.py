f1=open("file1.txt","r")

content= f1.readlines()

d=[]

s3=[]
s4=[]


print(content)

for i in content:
    
    c=i.split()
    d.extend(c)

print(d)

for i in d:
    s1=""
    s2=""
    for j in i:

        if j.isdigit():
            s1=s1+j
        else:
            s2=s2+j

    if s1:
        s3.append(s1)
    if s2:
        s4.append(s2)


print(s3)
print(s4)

s5=s4[0] +" "+s3[0]
s6=s4[1] +" "+s3[1]



print(s5)
print(s6)



    
    

    





  

    

  
        


