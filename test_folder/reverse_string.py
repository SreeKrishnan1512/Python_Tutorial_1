a="runs dog"


b=a.split()
c=len(b)


for i in range(c-1,-1,-1):
    d=b[i]
    print(d.swapcase())
