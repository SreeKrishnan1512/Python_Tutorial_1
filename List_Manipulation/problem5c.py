a=[]
b=[]
for i in range(65,91):
    c=chr(i)

    a.append(c)

print(a)
for i in range(97,97+26):
    c=chr(i) * (i-96)
    d= c
    b.append(d)

    

print(b)


