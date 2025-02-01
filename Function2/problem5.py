a=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
c=0
b=[]

day1=str(input("Enter the day: "))

for i in range(0,7):
  
    if a[i]==day1:
        c=i
        print(c)

for j in range(c,7):
    #print(a[j],end=" ")
    b.append(a[j])

d=a[0:c]
print(d)
print(b)

b.extend(d)
print(b) #b holds the values now

Day=int(input("Select a day from 1 to 365: "))

    
day_mod= Day%7
print(b[day_mod-1])

    





    
    
      


'''
if day1 in a:
    count=0
    for i in range(2,365):



else:
    print("Select the valid day")
'''
