phy = ['22mia1001','22mia1002','22mia1003','22mia1004']
chem = ['22mia1002','22mia1001','22mia1007','22mia1003']
math = ['22mia1001','22mia1010','22mia1007','22mia1003']
com = ['22mia1001','22mia1014','22mia1015','22mia1004']
n = set(phy)|set(chem)|set(math)|set(com)
print(len(n))
