num1 = int(input("Enter a Number"))
num2 = int(input("Enter a Number"))
num3 = int(input("Enter a Number"))

if num1 > num2:
    n = num1
elif num2 > num3:
    n = num2
else:
    n = num3

print(n)

nn = n**2
nnn = n**3


k = n+nn+nnn

print(f"n+nn+nnn={n}+{nn}+{nnn}= {k}")

radius = n
perimeter = 2*3.14*radius
area = 3.14*radius**2

print("Perimeter=", perimeter)
print("Area=", area)
