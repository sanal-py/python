import csv
f=open("name.csv","r")

content=csv.reader(f)
#next(content)
for i in content:
    if int(i[3])>=90:
        print(i[3])
f.close
