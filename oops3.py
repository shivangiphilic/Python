class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def Area(self):
        return(self.length*self.breadth)

class color_rectangle(Rectangle):
    def __init__(self,length,breadth,color):
        self.length = length
        self.breadth = breadth
        self.color = color

n = int(input("No. of rectangles: "))
areas = []
for i in range(n):
    l = int(input("Enter length: "))
    b = int(input("Enter breadth: "))
    c = input("Enter color: ")
    areas.append(color_rectangle(l,b,c))

c = areas[0].color
a = areas[0].Area()

for i in range(1,len(areas)):
    if(areas[i].Area() < a):
        ar = areas[i].Area()
        c = areas[i].color

print(f"Rectangle with min area is of {c} color")
