s=input("enter the string")
dict={}
for i in s:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
#print(dict.items())
for k,v in dict.items():
    print(k,"=",v)

