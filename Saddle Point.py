def saddle_point(mat, n):
    for i in range(n):
        min_row = mat[i][0]
        col_ind = 0
        for j in range(1, n):
            if (min_row > mat[i][j]):
                min_row = mat[i][j]
                col_ind = j
        k = 0
        for k in range(n):
            if (min_row < mat[k][col_ind]):
                break
            k += 1
        
        if (k == n):
            print("Value of Saddle Point ",min_row)
            return True;
 
    return False;

r = int(input("Enter the number of rows:"))
c = int(input("Enter the number of columns:"))

matrix = []
print("Enter the entries rowwise:")

for i in range(r):
    a =[]
    for j in range(c):
        a.append(int(input()))
    matrix.append(a)

for i in range(r):
	for j in range(c):
		print(matrix[i][j], end = " ")
	print()

saddle_point(matrix, len(matrix))
