print("Enter n: ")
n = int(input())
a=[]
b=[]
c=[]
print("Enter string 1: ")
for i in range(n):
    a.append(input())
print("Enter string 2: ")
for i in range(n):
    b.append(input())

print(a)
print(b)
c = a+b       # we can use - a.extend(b)
c.sort()
print(c)
