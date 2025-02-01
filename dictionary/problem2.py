dic= {}

for i in range(1,5):
   key=str(input("Enter the product name: "))
   value=int(input("Enter the price: "))

   dic[key]=value

print(dic)

while True:
    
   
        key=str(input("Enter the product you are searching for: "))

        if key not in dic:
            print(f"{key} product not found")
        else:
            print(f"{key} product found and the price is {dic[key]}")
   
   

