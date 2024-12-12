class rectangle:
    def __init__(self, length,breadth):
        self._length = length
        self._breadth = breadth

    def area(self):
        return self._length * self._breadth


    def __lt__(self, other):
        return self.area() < other.area()

print("\nEnter the dimensions")
l1=int(input("\nEnter the lenght"))
b1=int(input("\nEnter th breadth"))
rect1 = rectangle(l1,b1)
print("Area of Rectangle", rect1.area())


print("\nEnter the dimensions")
l2=int(input("\nEnter the lenght"))
b2=int(input("\nEnter th breadth"))
rect2 = rectangle(l2,b2)
print("Area of Rectangle", rect2.area())


print("\n Compare the areas")

if rect1.area() > rect2.area():
    print("Area of Rectangle1 is Larger")
elif rect1.area() < rect2.area():
    print("Area of Rectangle2 is Larger")
else:
    print("Area of two Rectangle is Equal")

