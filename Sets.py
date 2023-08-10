# Union '|'
# Intersection '&'
# Difference '-'

# s = set()
# s.add()
# ordering is not maintained in set, so no indexing and slicing
# Repeation also doesn't take place

"""
n = int(input("Enter number of elements: "))
s = set()
for i in range(n):
        val = int(input("Enter number: "))
        s.add(val) # using union.... s = s|{val}
print(s)
print(len(s))
"""

s1 = set()
s2 = set()
n = int(input("Enter number of elements in set_1: "))
for i in range(N):
    val = int(input("Enter number: "))
    s1.add(val)
print("\n")
n = int(input("Enter number of elements in set_2: "))
for i in range(N):
    val = int(input("Enter number: "))
    s2.add(val)

print(s1)
print(s2)
print("\n")
print("Union"+(s1|s2))
print("intersection"+(s1&s2))
print("Difference"+(s1-s2))
