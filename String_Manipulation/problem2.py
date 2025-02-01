a=str(input("Enter the string: "))
b=[]
c=[]

count=0
    
for i in range(0,len(a)):
          if(a[i].isdigit()):
            b.append(int(a[i]))
     
print(b)





for i in b:
      count=count+i

print(f" The total count of numbers in the string is {count}")

      







     
     



    

