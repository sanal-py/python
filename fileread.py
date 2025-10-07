def fread():
    f=open("demo.txt","r")
    data=f.read(3)
    print(data)
    f.close()
fread()
def freadline():
    f=open("demo.txt","r")
    
    data=f.readline()
    
    print(data)
    f.close()
freadline()

def freadlines():
    f=open("demo.txt","r")
    data=f.readlines()
    print(data)

freadlines()
