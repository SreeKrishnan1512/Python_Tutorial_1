import pickle

f1=open("demo.dat","wb")

for i in range(1,3+1):

    lst=eval(input("Enter the number: "))
    pickle.dump(lst,f1)

f1.close()

fr=open("demo.dat","rb")

while(True):
    try:
        data=pickle.load(fr)
        print(data)
    except:
        print("finished")
        break

fr.close()
