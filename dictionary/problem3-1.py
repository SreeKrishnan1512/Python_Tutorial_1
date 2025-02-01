dic={}
dic["January"]= 31
dic["February"]= 28
dic["March"]= 31
dic["April"]= 30
dic["May"]= 31

print(dic)

for key,value in dic.items():
    print(f"The key is '{key}' and the value is '{dic[key]}' ")


c=sorted(dic.values())
print(c)
