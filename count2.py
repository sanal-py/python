'''list=[1,2,3,4,5,]
sum=0
for i in  list:
    sum=sum+i

print(sum)'''


n=int(input("enter the no.of items"))
list=[]
for i in range (n):
      elements=int( input("enter the element"))
      list.append(elements)
print(list)
sum=0
for i in list:
    sum=sum+i
print(sum)
