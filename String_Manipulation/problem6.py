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

#max_str_div= max_string

max_string1=max_string[0 :3]

max_string2=max_string[3:6 ]

reverse_maxstr2=max_string2[::-1]

for i in range(0,max_len//2):

         maxstr1= max_string1[i]+ " " *(4-i)
         maxstr2=reverse_maxstr2[i]   
         result= maxstr1+" "+maxstr2
         print(result,end=" ") 
        #print("  "*i,max_string1[i]+"  "+reverse_maxstr2[i],end=" ")

         print("\n")




    



         



