#write a program to read a file line by line store it into a list
file=open("poem.txt","r")
cont=file.readlines()
linelist=[]
for i in cont:
    print(i)
    line=i.strip()
    linelist.append(line)
print(linelist)
file.close()

