""" The DNA sequence is made up of four chemical bases, Adenine (A), Cytosine (C),
Thymine (T), and Guanine (G). For a given DNA sequence like
“ATCTCAGTCGTTGTCTACATGA”, write a program to count the number of
Adenine, Cytosine, Thymine, and Guanine. Read any input from user and print the
output as dictionary which stores the Alphabet as key and its frequency as value. """

string = input("Enter DNA sequence: ")
l = []
a=c=g=t=0
for x in string:
    l.append(x)
    if(x=='A'):
        a=a+1
    elif(x=='C'):
        c=c+1
    elif(x=='G'):
        g=g+1
    else:
        t=t+1
print(l)
print("\n")
print("'A':"+str(a)+"'G':"+str(g)+"'C':"+str(c)+"'T':"+str(t))
