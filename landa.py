num = int(input("Enter the number:"))
list = [i for i in range(1, num+1)if num % i == 0]
print("factors of numbers=", list)

print("\nEnter length and breadth of a rectangle:")
l=int(input("length: "))
b=int(input("breadth: "))
c=lambda x,y: x*y
print("Area of rectangle: ",c(l,b))

print("\nEnter side of square:")
s=int(input("side: "))
c=lambda x: x*x
print("Area of square: ",c(s))