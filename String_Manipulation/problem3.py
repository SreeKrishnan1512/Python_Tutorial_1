#a="I wish to be successful in my life"
a="Good Morning"
count_words=1
count_letters=0
count_aplhanum=0
for i in range(0,len(a)):
    
    if(a[i]==" "):

      count_words=count_words+1

    

  
    
         

print(f"The count of words is {count_words}")


for i in range(0,len(a)):
    count_letters=i+1


print(f" The Number of characters are {count_letters}")


for i in range(0,len(a)):
   
   if(a[i].isalnum()):
      #print(a[i])
      count_aplhanum=count_aplhanum+1


percentOfAlpnum= (count_aplhanum/count_letters)*100

print(f" The Percentage of Alpha numeric is {percentOfAlpnum}")









