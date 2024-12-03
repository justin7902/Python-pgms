class rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b


    def area(self):
        return self.l*self.b


    def peri(self):
        return 2*(self.l+self.b)

    def display(self):
        print(f"\nArea of Rectangle: {self.area()}")
        print(f"\nPerimeter of Rectangle: {self.peri()}")

    def compare_area(self, other):
        if self.area() == other.area():
            print("\nArea of two Rectangles are equal")
        elif self.area() > other.area():
            print("\nArea of  rectangle1 is greater")
        else:
            print("\nArea of Rectangle2 is greater")

print("\nEnter the dimensions")
l1=int(input("\nEnter the lenght"))
b1=int(input("\nEnter th breadth"))
rect1 = rectangle(l1,b1)
rect1.display()


print("\nEnter the dimensions")
l2=int(input("\nEnter the lenght"))
b2=int(input("\nEnter th breadth"))
rect2 = rectangle(l2,b2)
rect2.display()


rect1.compare_area(rect2)