""" matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
matrix2 = [[1,2,3],[4,5,6],[7,8,9]]
matrix3 = matrix1 + matrix2 """

row = int(input("Enter no of rows: "))
col = int(input("Enter no of columns: "))
print("Enter the first matrix: ")
list1 = [[int(input()) for j in range(col)] for i in range(row)]     # we read matrix from row side, so row-for_loop should be on outer side
print("Enter the second matrix: ")
list2 = [[int(input()) for j in range(col)] for i in range(row)]
print(list1)
print(list2)
sum = [[list1[i][j] + list2[i][j] for j in range(col)] for i in range(row)]
print(sum)
""" for x in sum:
    print(sum) """
