class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def display(self):
        print(f"Rectangle: Length = {self.length}, Breadth = {self.breadth}")
        print(f"Area:", self.area())


def create_rectangle():
    length = float(input("Enter the length of the rectangle: "))
    breadth = float(input("Enter the breadth of the rectangle: "))

    rectangle = Rectangle(length, breadth)
    rectangle.display()

create_rectangle()
