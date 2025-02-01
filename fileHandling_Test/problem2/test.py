a=[[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13]]
b=[]

print(a)
for i in a:
    b.extend(i)

    

print(b)

c=[]
separateList=[]

for i in range(0,len(b),5):
    #print(b[i],end=" ")
    if i+1 < len(b):
        d= [b[i],b[i+1],b[i+2],b[i+3],b[i+4]]
        c.append(d)
        
    else:
        separateList.append(b[i])
        c.append(separateList)
        

print(c)

