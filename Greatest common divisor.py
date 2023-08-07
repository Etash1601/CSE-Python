#Import math Library
import math

# find the  the greatest common divisor of the two integers
print (math.gcd(120, 250))

# in other way
m = int(input())
n = int(input())
for i in range(m,0,-1):
    if(m%i==0) and (n%i==0):
        print(i)
        break;
