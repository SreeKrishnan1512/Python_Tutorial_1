n = int(input("Enter the input digits: "))
c=[]

for i in range(n):
    digits= int(input(f"Enter the Number {i+1}: "))
    c.append(digits)

print(c)

c.sort()
c.reverse()
print(c)

highest_num= c[0]
print(f"The highest number is {highest_num}")



