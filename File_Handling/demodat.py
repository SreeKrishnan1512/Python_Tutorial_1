import pickle

f1=open("demo.dat","wb")

for i in range(0,3):

    n=eval(input("Enter the number: "))

    pickle.dump(n,f1)

f1.close()

f2= open("demo.dat","rb")


while True:
    try:
        c=pickle.load(f2)
        print(c)

    except:
        print("finished")
        break