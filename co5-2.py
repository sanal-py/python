f=open("poem.txt","r")
content=f.readlines()
a=len(content)
feven=open("evenfile.txt","a")
fodd=open("oddfile.txt","a")

for i in range(a):
    if i%2==0:
      print(content[i])
      fodd.write(content[i])
    else:
      feven.write(content[i])


f.close()
fodd.close()
feven.close()

