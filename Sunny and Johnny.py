print("Enter n: ")
n = int(input())
a=[]
print("Enter List: ")
for i in range(n):
    a.append(int(input()))
print(a)
for i in range(n-1):
    for j in range((i+1),n):
        if(a[i]+a[j]==30):
            print("%d and %d add upto 100"%(i,j))
