"""a=()
n = int(input())
for i in range(n):
    s = int(input())
    a = a+(s,)
print(a)"""

t=()
n = int(input())
for i in range(n):
    t = t + ((int(input())**2),)

print(t)
a = sorted(t)
print(a)
