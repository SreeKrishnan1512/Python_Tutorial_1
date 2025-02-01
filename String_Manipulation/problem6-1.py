a=str(input("Enter the string: "))

b=str(input("Enter the string: "))

c=len(a)

d=len(b)

if(len(a)>len(b)):

    max_len=len(a)
    max_string=a

    min_len=len(b)
    min_string=b


else:
    max_len=len(b)
    max_string=b

    min_len=len(a)
    min_string=a


print(min_string)

for i in range(0, max_len//2):

    for j in range(0,max_len):
        
        if(i==j and max_len-i):
        
           print()