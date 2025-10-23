import csv
f=open("name22.csv","a",newline="")
content=csv.writer(f)

for i in range(2):
    name=input("enter the name")
    age=int(input("enter the age"))
    mark=float(input("enter the mark"))
    rec=[name,age,mark]
   
    content.writerow(rec)

f.close()

f1=open("name22.csv","r")
content=csv.reader(f1)
next(content)
for i in content:
    print(i)
    
