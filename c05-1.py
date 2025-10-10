#write a program to create  a class rectangle with atributes length and breadth to find area and perimeter
class rectangle():
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    def area(self):
        return self.breadth*self.length
    def perimeter(self):
        return 2*(self.length+self.breadth)
a=int(input("enter the length of first rectangle"))
b=int(input("enter the first of breadth rectangle"))    
obj1=rectangle(a,b)

c=int(input("enter the length of second rectangle"))
d=int(input("enter the breadth of second rectangle"))
obj2=rectangle(c,d)

area1=obj1.area()
area2=obj2.area()
print("area of rectangle1:",area1)
print("area of rectangle1:",area2)
perimetre1=obj1.perimeter()
perimetre2=obj2.perimeter()

#compare the area
if area1>area2:
    print("rectangle 1 has largest area")
elif area1<area2:
    print("rectangle 2 has largest area")
else:
    print("rectangle 1 and 2 has same area")


print("perimetre of rectangle1:",obj1.perimeter())
print("perimetre of rectangle2:",obj2.perimeter())
    
    
    





      
      
