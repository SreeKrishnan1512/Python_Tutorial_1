

a=[[2,3,7],[4,5,6],[7,8,9]]

b=[]

c=[]


for i in a:

    b.extend(i) #Extend should be used only for list

print(b)

count=5

for i in range(0, len(b), count):
    d = b[i:i+count]  # Slice two elements at a time
    c.append(d)

print("Result:", c)





    
