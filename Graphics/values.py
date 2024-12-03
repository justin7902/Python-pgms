from Graphics import rectangle, circle
from Graphics.dgraphics import cuboid, sphere

l = int(input("Enter the length\n"))
b = int(input("Enter the breadth\n"))

rectangle.rect_area(l,b)
rectangle.rect_peri(l,b)


r = int(input("Enter the radius\n"))

circle.cir_area(r)
circle.rect_peri(r)


r = int(input("Enter the radius\n"))

sphere.sph_area(r)
sphere.sph_peri(r)


l = int(input("Enter the length\n"))
b = int(input("Enter the breadth\n"))
h = int(input("Enter the height\n"))

cuboid.peri_cub(l,b,h)
cuboid.area_cub(l,b,h)
