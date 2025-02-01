sum=0
count=0
for i in range(1,21,2):
    count=count+1
    sum=sum+((-(-1)**count)/i)

    print(sum)

 
print(f"The final sum is {sum}")
print(f"Loop iterated over {count} times")
