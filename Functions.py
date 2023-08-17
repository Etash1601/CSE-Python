# Functions
"""int add(int a, int b)
{
    return(a+b);
}
int x=15, y=20;
int total = add(x,y);"""

# def = definition of function
"""
there's no return type

def add(a,b):
    return(a+b)
x=int(input())
y=int(input())
print(add(x,y))
"""

# 3 types of arguement passes
"""
1. Positional { add(10,30,15) }
2. keyword { add(a=10,b=30,c=15) }
3. Default { def add(10,20,c=30,d=40)
             total = add(10,20) }


def add(a,b,c=30,d=40):
    tot = a+b+c+d
    avg = tot/3
    return tot,avg
# returning more than 1 variable is taken as tuple
print(add(10,20))
"""
"""
l=[]
n=5
for i in range(n):
    l=l+[int(input())] # l.append(int(input())

def list(k):
    k.sort()
    avg = sum(k)/len(k)
    return (k,avg)

d,average = list(l)
print(d)
print(average)

# more than 1 type of variable and unknown length
def func(*t):   *t=tuple
def func2(**t):  **t=dictionary

def add(a,*t)
add(10,20,30)    # *t=(20,30)
"""
"""
# Recursive factorial
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))

# Recursive Greatest Common Divisor
def gcd(a,b):
    if a%b==0:
        return b
    else:
        return gcd(b,a%b)
    
print(gcd(100,60))

# Lambda Function
x = lambda a: a+10
print(x(5))

Maxnum = lambda a,b: a if(a>b) else b
print(Maxnum(5,4))
"""
