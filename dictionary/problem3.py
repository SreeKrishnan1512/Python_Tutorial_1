dic={}
for i in range(1,5+1):
    key=input("Enter the month: ")
    value= int(input("Enter the number of days: "))
    dic[key]=value

print(dic)

for i in sorted(dic):
   print(f"The Sorted months are {i} along with days {dic[i]}")

for key,value in dic.items():
    if value == 31:
        print(key)

for key,value in sorted(dic.items(), key= lambda item : item[1]):
    print(f"The sorting of months {key} is done based on the number of days in that month {dic[key]}")


        


