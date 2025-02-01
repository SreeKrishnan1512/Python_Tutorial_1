a=[1,2,0,3,0,4,5]

b= [x for x in a if x!=0] +[x for x in a if x==0]


print(b)