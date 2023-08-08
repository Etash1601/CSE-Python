# Union '|'
# Intersection '&'
# Difference '-'

# s = set()
# s.add()
# ordering is not maintained in set, so no indexing and slicing
# Repeation also doesn't take place

n = int(input("Enter number of elements: "))
s = set()
for i in range(n):
        val = int(input("Enter number: "))
        s.add(val) # using union.... s = s|{val}
print(s)
print(len(s))
