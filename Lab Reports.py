report=()
n=5
min = (20,35.5,12,120,80)
max = (30,40,15,150,120)
print("Enter the values: ")
for i in range(n):
    report = report + (input(),) # taking input as string

print(report)
print("Lab Report\n")
for i in range(n):
    if(report[i]=='N'):
        print("Test "+str(i+1)+" is not performed") # 'str(i+1)' converting into string to directly use in b/w the string
        continue # to move on to next values

    if((float(report[i])>=min[i]) and (float(report[i])<=max[i])):
        print("Test "+str(i+1)+" is normal")
    else:
        print("Test "+str(i+1)+" is not normal")
