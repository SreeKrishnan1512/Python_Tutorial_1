import csv

fhw1=open("excel3.csv","w",newline="\n")

f1= csv.writer(fhw1)

f1.writerow(["S.no","Name","Mark"])
f1.writerow(["1","Alice",60])
f1.writerow(["2","Bob",70])
f1.writerow(["3","Carl",80])
f1.writerow(["4","David",90])
f1.writerow(["5","Evangeline",100])

fhw1.close()

fhr1=open("excel3.csv","r")

fhw2=open("excel4.csv","w",newline="\n")
f3=csv.writer(fhw2)

f2=csv.reader(fhr1)

for row in f2:
    if row[0] !="3" :
        if row[1]=="David":
            row[1]="Beckham"
            #f3.writerow(row[1])
        
        f3.writerow(row)

    




