def AddMatrix(A,B):
    result = [[A[i][j] + B[i][j]  for j in range(len(A[0]))] for i in range(len(A))]
    print("Addition of Two Matrices: ")
    for r in result:
        print(r)

def SubMatrix(A,B):
    result = [[A[i][j] - B[i][j]  for j in range(len(A[0]))] for i in range(len(A))]
    print("Subtraction of Two Matrices: ")
    for r in result:
        print(r)

def MultMatrix(A,B):
    result = [[0 for col in range(ColumnNo)] for row in range(RowNo)]
    for i in range(len(A)):
        for j in range(len(B[0])):
           for k in range(len(B)):
               result[i][j] += A[i][k] * B[k][j]
    print("Multiplication of Two Matrices: ")
    for r in result:
        print(r)

def Transpose(A):
    result = [[0 for col in range(ColumnNo)] for row in range(RowNo)]
    for i in range(len(A)):
       for j in range(len(A[0])):
           result[j][i] = A[i][j]
    print("Transposed of Matrix: ")
    for r in result:
        print(r)

RowNo = int(input("Input number of rows: "))
ColumnNo = int(input("Input number of columns: "))

A = [[0 for col in range(ColumnNo)] for row in range(RowNo)]
for row in range(RowNo):
    for col in range(ColumnNo):
        item = int(input("Enter the elements in first matrix: "))
        A[row][col]= item
print("\nMatrix 1: ")
print(A)

B = [[0 for col in range(ColumnNo)] for row in range(RowNo)]
for row in range(RowNo):
    for col in range(ColumnNo):
        item = int(input("Enter the elements in second matrix: "))
        B[row][col]= item
print("\n 2: ")
print(B)

print("\nSelect Matrix Operation")
print("1. Addition of Two Matrices")
print("2. Subtraction of Two Matrices")
print("3. Multiplication of Two Matrices")
print("4. Transpose of Matrix")
print("5. Exit ")

while True:
    choice = int(input('\nEnter your choice: '))

    if choice == 1:
        AddMatrix(A,B)

    elif choice == 2:
        SubMatrix(A,B)

    elif choice == 3:
        MultMatrix(A,B)

    elif choice == 4:
        Transpose(A)

    elif choice == 5:
        print("Exit!")
        break
    else:
        print("Invalid Input")
