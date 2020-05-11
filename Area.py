print("calculate area\n".upper())

def calcarea_triangle(a,b):
    return (a*b)/2
def calcarea_circle(r):
    return r*3.14159
print("triangle".upper())
a=float(input("enter the height: "))
b=float(input("enter the width: "))
print("area is "+str(calcarea_triangle(a,b)))
print("circle".upper())
r=float(input("enter the radius: "))
print("area is "+str(calcarea_circle(r)))
