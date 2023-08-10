# pair of items - each pair has key and value, separated by :
# key should be unique

students = {'22mia1002':'xyz','22mia1003':'abc'}
print(students.keys())
print(students.values())
print(students['22mia1002'])  # prints the key's value 

D = {}
D[99] = 'spam' # even if dictionary is empty, we can assign value on particular key
print(D) 

d = {}
n = int(input())
for i in range(n):
    k = input("Reg no: ")
    v = input("Name: ")
    d[k]=v
print(d)
