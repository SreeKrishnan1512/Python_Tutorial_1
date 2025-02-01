from datetime import datetime

n=str(input("Enter the Date in MM/DD/YYYY: "))

M= n[0:2]
m=int(M)
D=n[2:4]
d=int(D)
Y=n[4:]
y=int(Y)

date=datetime(y,m,d)

print(f"Full Date: {date.strftime('%A, %B %d, %Y')}")
