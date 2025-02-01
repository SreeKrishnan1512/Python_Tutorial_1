Which_Tables= int(input("Enter which table you want to multiply: "))
upto= int(input("upto which value say for example 5*10: "))
d=[]

for i in range(1, upto+1):
    c=Which_Tables*i
    d.append(c)

print(d)