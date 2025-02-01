a=["Hi","How","Are","You","Doing","Bujji","?"]


max_length=0

maxlen_word=[]


for i in range(0,len(a)):
    b=a[i]
    

    
    count=0
    
    for j in b:
      
      count=count+1

    print(f"The word '{b}' has length of {count}")
    
    if count>max_length:
   
      max_length= count
      maxlen_word=[b]
    
    elif count==max_length:
       maxlen_word.append(b)

    print(f"The maximum length word is '{maxlen_word}' with count of {max_length}")





    



    





