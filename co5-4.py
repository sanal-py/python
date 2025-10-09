import csv
f=open("book1.csv","r")
content=csv.reader(f)
for i in content:
    x=int(input("enter the index"))
    print(i[x])

