import csv

fh=open("demo.csv","w",newline='\n')

f1=csv.writer(fh)

f1.writerow(["RollNo","Name","Marks"])
f1.writerow(["1","abc",100])
f1.writerow(["2","def",100])
f1.writerow(["3","ghi",100])
f1.writerow(["4","jkl",100])
f1.writerow(["5","mno",100])
fh.close()

fr=open("demo.csv","r")
data=csv.reader(fr)
#next(data)
for i in data:
    print(i)
fr.close()