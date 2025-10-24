#Accept a list of word and return the length of longest word
list=[]
limit=int(input("enter the limit"))
for i in range(limit):
    word=input("enter the word")
    list.append(word)
print(list)
length=0
for i in list:
    #print(len(i))
    if len(i)>=length:
        longest=i
        length=len(i)
print("The greatest word:",longest)
print("length of word",length)

