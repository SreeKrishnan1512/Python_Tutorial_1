
for i in range(2,100):
        count = 0
        for j in range(1,i):
            if (i%j==0 ):
                count = count +1
        if count == 1:
             print(i)
            