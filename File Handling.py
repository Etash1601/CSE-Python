# procedure to open a file
# 1)
f1 = open("note.txt","r")
print("Name of the file: ",f1.name)
print("Closed or not: ",f1.closed)
print("Opening mode: ",f1.mode)

# 2)
f = open("filesample.txt","r")
fcontent = f.read()
print(len(fcontent))
f.seek(0) # to again read from the start
flines = f.readlines()
print(len(flines))
f.close

# 3)
f = open("filesample.txt","w")
f.write("Hello")
f.close
f = open("filesample.txt","r")
fcontent = f.read()
print(fcontent)
