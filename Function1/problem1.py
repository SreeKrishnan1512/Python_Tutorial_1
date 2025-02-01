def USDtoINR():
   
        USD= int(input("Enter the USD amount: "))
        INR= USD * 85 
        print(f"${USD} converted to INR Rs.{INR} ")
        return INR

c= USDtoINR()

def Check():
        print(f"This is inside check function {c}")

Check()


        
