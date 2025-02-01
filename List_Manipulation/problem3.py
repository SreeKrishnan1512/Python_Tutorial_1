n=12

lists=[]
for i in range(1,n+1):

    value= int(input(f"Enter the value for {i}: "))
    lists.append(value)


for i in range(0,len(lists)):
    
  if(lists[i]>10):
     lists[i]=10


print(lists)
