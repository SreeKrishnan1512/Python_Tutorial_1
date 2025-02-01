f1=open("event1.txt","r")
f2=open("event2.txt","w")
content=f1.readlines()

print(content)
List1=[]
List2=[]

for i in content:

    c=i.split()
    for j in c:
        List1.append(j)

print(List1)

print(len(List1))

for i in range(0,len(List1)):
    if List1[i]=="Athletics":
        c=[List1[i],List1[i+1]]
        List2.append(c)

list3=[]

for i in List2:
    list3.extend(i)

print(list3)

for i in range(0,len(list3),2):

    c=list3[i]+" = "+list3[i+1]
    f2.write(c)
    f2.write("\n")








    








 



   
    