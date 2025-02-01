c=[]

for i in range(10,50):
    if (i%3==0 and i%4==0):
        c.append(i)
    else:
        continue
print(c)