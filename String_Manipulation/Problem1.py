a=str(input("Enter the string: "))
b=[]

for i in range(0,len(a)):

  b.append(a[i])


  
if(a[3]=="-" and a[7]=="-"):
    print(f"- is valid")
    
else:
    print(f"- is not valid")

    
if(a[0:3].isdigit() and a[4:7].isdigit() and a[8: ].isdigit()):
    
    print("Number is valid")

else:
     print("Number is not valid")
    


    