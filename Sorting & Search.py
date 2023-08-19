l=[]
n=int(input("Enter the length of the list: "))
for i in range(n):
    l.append(int(input("Enter Element "+str(i+1)+": ")))

for i in range(n):
    for i in range(n-1):
        if(l[i]>l[i+1]):
            temp = l[i]  # l[i], l[i+1]=l[i+1], l[i]
            l[i]=l[i+1]
            l[i+1]=temp

print(l)

a=int(input("Enter the number to be searched: "))
for i in range(n):
    if(a==l[i]):
        print(str(a)+" is in the position "+str(i+1))
