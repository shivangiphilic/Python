class Polygon:
    def get_Triangle(self):
        self.base = int(input("Enter base of triangle: "))
        self.height = int(input("Enter height of triangle: "))
    
    def get_Rectangle(self):
        self.s1 = int(input("Enter one side of rectangle: "))
        self.s2 = int(input("Enter other side of rectangle: "))

    def get_Square(self):
        self.s = int(input("Enter side of square: "))

class Triangle(Polygon):
    def Area(self):
        print("Area of Triangle:",0.5*self.base*self.height)

class Rectangle(Polygon):
    def Area(self):
        print("Area of Rectangle:",self.s1*self.s2)

class Square(Polygon):
    def Area(self):
        print("Area of Square:",self.s*self.s)

t = Triangle()
r = Rectangle()
s = Square()
t.get_Triangle()
r.get_Rectangle()
s.get_Square()
t.Area()
r.Area()
s.Area()