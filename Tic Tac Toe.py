row = 3
col = 3
print("Enter the matrix: ")
matrix = [[int(input()) for j in range(col)] for i in range(row)]
for x in matrix:
    print(matrix)

if(matrix[0][0]==1 and matrix[0][1]==1 and matrix[0][2]==1):
    winner = 1
elif(matrix[0][0]==2 and matrix[0][1]==2 and matrix[0][2]==2):
    winner = 2

if(matrix[0][0]==1 and matrix[1][1]==1 and matrix[2][2]==1):
    winner = 1
elif(matrix[0][0]==2 and matrix[1][1]==2 and matrix[2][2]==2):
    winner = 2

if(matrix[2][0]==1 and matrix[1][1]==1 and matrix[0][2]==1):
    winner = 1
elif(matrix[2][0]==2 and matrix[1][1]==2 and matrix[0][2]==2):
    winner = 2

if(matrix[2][0]==1 and matrix[2][1]==1 and matrix[2][2]==1):
    winner = 1
elif(matrix[2][0]==2 and matrix[2][1]==2 and matrix[2][2]==2):
    winner = 2

print("Winner is User %d"%winner)
