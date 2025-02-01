n=int(input("enter the value of n: "))
count=n-1

for i in range(1,n+1):

  for j in range(1,n+1):
      
      if (j<=count):
         print("-",end=' ')
      else:
         print(j-count, end=" ")
  count=count-1
  print("\n")