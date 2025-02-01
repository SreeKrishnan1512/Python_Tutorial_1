

#f1=open("demo.txt","r")
li= [1,2,3,4]
f1=open("li","wb")

try:

    while(True):
        readlin=f1.readline()
        print(readlin)
        x=(input(""))

except:
    print("finished")
