row = 3
col = 3
print("Enter the matrix: ")
matrix = [[int(input()) for j in range(col)] for i in range(row)]
winner = 0

for x in matrix:
    print(matrix)

for i in range(0,3): # i is for rows
    if(matrix[i][0]==1 and matrix[i][1]==1 and matrix[i][2]==1):
        winner = 1
    elif(matrix[i][0]==2 and matrix[i][1]==2 and matrix[i][2]==2):
        winner = 2

for j in range(0,3):  # j is for columns
    if(matrix[0][j]==1 and matrix[1][j]==1 and matrix[2][j]==1):
        winner = 1
    elif(matrix[0][j]==2 and matrix[1][j]==2 and matrix[2][j]==2):
        winner = 2
    
# Diagonals
if(matrix[0][0]==1 and matrix[1][1]==1 and matrix[2][2]==1):
    winner = 1
elif(matrix[0][0]==2 and matrix[1][1]==2 and matrix[2][2]==2):
    winner = 2

if(matrix[2][0]==1 and matrix[1][1]==1 and matrix[0][2]==1):
    winner = 1
elif(matrix[2][0]==2 and matrix[1][1]==2 and matrix[0][2]==2):
    winner = 2

print("Winner is User %d"%winner)
