# 1)
class student:
    def __init__(self,n,a):  # constructor
        self.full_name = n
        self.age = a

s1 = student("XYZ",25)
s2 = student("ABC",32)
print(s1.age)
print(s2.age)

# 2)
class room:
    length = int(input("Enter the length: "))
    breadth = int(input("Enter the breadth: "))

    def calculatearea(self):
        area = self.length*self.breadth;
        print("Area of the room : ",area)

Area = room()
Area.calculatearea()

# 3)
class Student:

    def __init__(self,name,mark1,mark2):
        self.name = name
        self.mark1 = mark1
        self.mark2 = mark2

    def average(self):
        return (self.mark1+self.mark2)/2

    def print_data(self):
        print(self.average())

David = Student("David",90,100)
Bob = Student("Bob",60,80)
David.print_data()  # self represents David
Bob.print_data()  # self represents Bob


# 4)
# Array of objects

class student:
    counter = 0
    def __init__(self,n,a):
        self.name = n
        self.age = a
        student.counter = student.counter + 1
        # self is of no use as we are only counting

s=[] # list of student object
n = int(input("Enter the no of students: "))
for i in range(n):
    name = input("Enter the name: ")
    age = int(input("Enter age: "))
    s.append(student(name,age))
    # entering value in list as array of objects
print(s)
for i in range(n):
     print("Name: "+s[i].name,"   Age: ",s[i].age)

for i in range(n):
    for j in range(i+1,n):
        if(s[i].age > s[j].age):
            s[j],s[i] = s[i],s[j]
print("\n")
print("After Sorting")
for i in range(n):
     print("Name: "+s[i].name,"   Age: ",s[i].age)
