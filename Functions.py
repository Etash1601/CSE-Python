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
print(add(10,20))"""

