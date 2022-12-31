def accept(r,c,mat):
    for i in range(0,r):
        temp=[]
        for j in range(0,c):
            element=int(input("Enter No. Of Elements"))
            temp.append(element)
        mat.append(temp)
def add(r,c,mat1,mat2):
    mat_add=[]
    for i in range(0,r):
        temp=[]
        for j in range(0,c):
            temp.append(mat1[i][j]+mat2[i][j])
        mat_add.append(temp)
    print("Addition: ")
    display(mat_add)
def subtract(r,c,mat1,mat2):
    mat_sub=[]
    for i in range(0,r):
        temp=[]
        for j in range(0,c):
            temp.append(mat1[i][j]-mat2[i][j])
        mat_sub.append(temp)
    print("Subtraction: ")
    display(mat_sub)
def display(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            print(mat[i][j], end = " ")
        print()
def mult(mat1,mat2):
    mat3=[]
    for i in range(len(mat1)):
        temp=[]
        for j in range(len(mat2[0])):
            temp.append(0)
        mat3.append(temp)
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                mat3[i][j]+=mat1[i][k]*mat2[k][j]
    print("Multiplication: ")
    display(mat3)
def transpose(mat):
    transpose=[]
    for i in range(len(mat)):
        temp=[]
        for j in range(len(mat[0])):
            temp.append(0)
        transpose.append(temp)
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            transpose[j][i]=mat[i][j]
    display(transpose)
def main():
    r1=int(input("Enter No. of Rows of 1st Matrix: "))
    c1=int(input("Enter No. of Columns of 1st Matrix: "))
    mat1=[]
    accept(r1,c1,mat1)
    display(mat1)
    print("Transpose of 1st Matrix: ")
    transpose(mat1)
    r2=int(input("Enter No. of Rows of 2nd Matrix: "))
    c2=int(input("Enter No. of Columns of 2nd Matrix: "))
    mat2=[]
    accept(r2,c2,mat2)
    display(mat2)
    print("Transpose of 2nd Matrix: ")
    transpose(mat2)
    add(r1,c1,mat1,mat2)
    subtract(r1,c1,mat1,mat2)
    mult(mat1,mat2)
    
main()
