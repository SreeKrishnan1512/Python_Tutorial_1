sum=0
x=2
fact=1
for i in range(0,4):
   
   if(i==0):
      fact=1
      sum=sum+((x**i)/fact)
      print(sum)
   else:
      fact=fact*i
      sum=sum+(((-x)**i)/fact)
      print(sum)
   
   
