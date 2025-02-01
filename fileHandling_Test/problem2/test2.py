a=[[2,3,7],[4,5,6],[7,8,9]]

b=[]

c=[]
separate=[]

for i in a:

    for j in i:

        b.append(j)

print(b)



for i in range(0,len(b),2):


    if i+1<len(b):
       
        d=[b[i],b[i+1]]
        c.append(d)

    else:
       separate.append(b[i])
       c.append(separate)

print(c)            
       
        


    
