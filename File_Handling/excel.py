import csv

fh=open("excel.csv","w",newline="\n")
f1=csv.writer(fh)

f1.writerow(["S.no","Name","Mark"])
f1.writerow(["1","Alice",60])
f1.writerow(["2","Bob",70])
f1.writerow(["3","Carl",80])
f1.writerow(["4","David",90])
f1.writerow(["5","Evangeline",100])

fh.close()

fhr=open("excel1.csv","r")

f2=(csv.reader(fhr))

fhw2=open("excel2.csv","w",newline="\n")
f3=csv.writer(fhw2)
#print(len(f2))

'''
for i in f2:
    print(i)
'''
f3.writerow(["S.No","Name","Mark"])
next(f2)
for row in f2:  # Skip the header row
    if int(row[2]) >= 90:  # Access the "Mark" column (third element in the sublist)
        f3.writerow(row)  # Print the name of the student
    
fhr.close()
