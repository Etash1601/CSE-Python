# Student Details
d={}
n = int(input("Enter number of students: "))
for i in range(n):
    regno = input("Enter reg no: ")
    name = input("Enter the name: ")
    a = input("Enter CAT_1 marks: ")
    b = input("Enter CAT_2 marks: ")
    c = input("Enter FAT marks: ")
    d[regno]=[name,a,b,c]

print(d)
