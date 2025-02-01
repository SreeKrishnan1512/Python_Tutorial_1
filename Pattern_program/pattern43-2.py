
count=0
n=int(input("Enter the number: "))

for i in range(1,n+1):
    for j in range(1,i+1):
        count=count+1

print("Total count is ",count)

print("\n")

c= count-n+1
a=c
for i in range(n,0,-1):
    d=c-i+1
    for j in range(1,i+1):
        print(c,end=" ")
        c=c+1
    c= d
    a=c
    print("\n")