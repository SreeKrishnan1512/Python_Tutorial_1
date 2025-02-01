fact=0
c=[]
for i in range(1,4+1):
    fact=fact+i
    c.append(fact)

print(c)

d=[]
for i in range(0,3+1):
    if i%2==0 :
       
       d.append(c[i])
    else:
        d.append(-c[i])

print(d)

sum=0
for i in d:
    sum= sum+i
print(sum)

  
