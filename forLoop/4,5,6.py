c=[]
for i in range(5,101):
    if(i%4==0 and i%5==0 and i%6==0):
        c.append(i)
    else:
        continue
print(c)