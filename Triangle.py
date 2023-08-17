import math
x1=5
y1=10
x2=20
y2=10
x3=15
y3=15
side1 = ((x2-x1)**2 + (y2-y1)**2)**0.5
# side1 = math.sqrt((x2-x1)**2 + (y2-y1)**2)
side2 = ((x3-x2)**2 + (y3-y2)**2)**0.5
side3 = ((x1-x3)**2 + (y1-y3)**2)**0.5
print("Side-1: %f"%(side1))
print("Side-2: %f"%(side2))
print("Side-3: %f"%(side3))
def triangle(a,b,c):
    if(a+b>=c and b+c>=a and c+a>=b):
        print("Triangle is valid")
    else:
        print("Triangle is not valid")

triangle(side1,side2,side3)
