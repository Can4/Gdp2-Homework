
def printMatrix(m):
    for line in m:
        print('|', end='')
        i = 0
        for value in line:
            if (i > 0):
                print(' ', end='')
            print(value, end='')
            i = i + 1
        print("|")

def matMultDef(a,b):
    print("\nmatMultDef :")
    temp = 0
    height_c = len(a)
    width_c = len(b[0])
    c = [[0 for x in range(width_c)] for y in range(height_c)]
    for i in range(len(a)):
        for j in range(len(b[0])):
            temp = 0
            for k in range(len(b)):
                temp = temp + (a[i][k] * b[k][j])
            c[i][j] = temp
        printMatrix(c)
        print()
    print("Berechnet matMultDef :")
    printMatrix(c)
    return c
#
# Dividing a given matrix into 4 sub-matrices
#
def divide(A):
    i = len(A)
    j = len(A[0])
# Berechnung Zeilenmitte von A  -- zm_A
# Berechnung Spaltenmitte von A -- sm_A
    zm_A = (i-1) // 2
    sm_A = (j-1) // 2

#  für i gerade - j gerade
    if (i%2)==0 and (j%2)==0 :
        height_A = i // 2
        width_A = j // 2
        A11 = [[0 for x in range(width_A)] for y in range(height_A)]
        A12 = [[0 for x in range(width_A)] for y in range(height_A)]
        A21 = [[0 for x in range(width_A)] for y in range(height_A)]
        A22 = [[0 for x in range(width_A)] for y in range(height_A)]

#  für i ungerade - j gerade
    if (i%2)==1 and (j%2)==0 :
        height_A = i // 2
        width_A = j // 2
        A11 = [[0 for x in range(width_A)] for y in range(height_A+1)]
        A12 = [[0 for x in range(width_A)] for y in range(height_A+1)]
        A21 = [[0 for x in range(width_A)] for y in range(height_A)]
        A22 = [[0 for x in range(width_A)] for y in range(height_A)]

#  für i gerade - j ungerade
    if (i%2)==0 and (j%2)==1 :
        height_A = i // 2
        width_A = j // 2
        A11 = [[0 for x in range(width_A+1)] for y in range(height_A)]
        A12 = [[0 for x in range(width_A)] for y in range(height_A)]
        A21 = [[0 for x in range(width_A+1)] for y in range(height_A)]
        A22 = [[0 for x in range(width_A)] for y in range(height_A)]

#  für i ungerade - j ungerade
#  i == j
    if i==j and (i%2)==1 and (j%2)==1 :
        height_A = i // 2
        width_A = j // 2
        A11 = [[0 for x in range(width_A+1)] for y in range(height_A+1)]
        A12 = [[0 for x in range(width_A)] for y in range(height_A+1)]
        A21 = [[0 for x in range(width_A+1)] for y in range(height_A)]
        A22 = [[0 for x in range(width_A)] for y in range(height_A)]

#  für i ungerade - j ungerade
#  i<j OR i>j
    if (i>j or i<j) and (i%2)==1 and (j%2)==1 :
        height_A = i // 2
        width_A = j // 2
        A11 = [[0 for x in range(width_A+1)] for y in range(height_A+1)]
        A12 = [[0 for x in range(width_A)] for y in range(height_A+1)]
        A21 = [[0 for x in range(width_A+1)] for y in range(height_A)]
        A22 = [[0 for x in range(width_A)] for y in range(height_A)]
#
# inserting values from A into the newly created sub-matrices A11,A12,A21,A22
#
    x = -1
    for k in range(0,zm_A+1):
        x += 1
        y = 0
        for t in range(0,sm_A+1):
            A11[x][y] = A[k][t]
            y +=1
    x = -1
    for k in range(0,zm_A+1):
        x += 1
        y = 0
        for t in range(sm_A+1,len(A[0])):
            A12[x][y] = A[k][t]
            y +=1
    x = -1
    for k in range(zm_A+1,len(A)):
        x += 1
        y = 0
        for t in range(0,sm_A+1):
            A21[x][y] = A[k][t]
            y +=1
    x = -1
    for k in range(zm_A+1,len(A)):
        x += 1
        y = 0
        for t in range(sm_A+1,len(A[0])):
            A22[x][y] =A[k][t]
            y +=1

    return A11,A12,A21,A22


def Add_Matrices(A,B) :
    result = [[0 for x in range(len(B[0]))] for y in range(len(A))]
    for i in range(len(A)):
       for j in range(len(A[0])):
           result[i][j] = A[i][j] + B[i][j]
    return result


def matMultDC(A,B):
# Zeilen und Spalten von A und B
    Ai = len(A)
    Aj = len(A[0])
    Bi = len(B)
    Bj = len(B[0])

#   Exit conditions
#
# --> (1x1) * (1x1)
    if (Ai ==1 and Aj ==1) and (Bi == 1 and Bj==1):
        return [[ A[0][0]*B[0][0] ]]
# --> (1xn) * (nx1)
    elif (Ai==Bj==1):
        temp = 0
        for k in range(0,Aj):
            temp = temp + A[0][k] * B[k][0]
        C = [[temp]]
        return C
# --> (nx1) * (1xn)
    elif (Aj==Bi==1) and (Ai==Bj):
        C = [[0 for x in range(Ai)] for y in range(Ai)]
        for k in range(0,Ai):
            for t in range(0,Ai):
                C[k][t] = A[k][0] * B[0][t]
        return C
# --> (nx1) * (1xm)
    elif (Aj==Bi==1):
        C = [[0 for x in range(Bj)] for y in range(Ai)]
        for k in range(0,Ai):
            for t in range(0,Bj):
                C[k][t] = A[k][0] * B[0][t]
        return C
# --> (2x2) * (2x1)
    elif (Aj==Bi==2) and (Ai == 2 and Bj ==1):
        C = [[0 for x in range(Bj)] for y in range(Ai)]
        C[0][0] = A[0][0]*B[0][0] + A[0][1]*B[1][0]
        C[1][0] = A[1][0]*B[0][0] + A[1][1]*B[1][0]
        return C
# --> (1x2) * (2x2)
    elif (Aj==Bi==2) and (Ai == 1 and Bj == 2):
        C = [[0 for x in range(Bj)] for y in range(Ai)]
        C[0][0] = A[0][0]*B[0][0] + A[0][1]*B[1][0]
        C[0][1] = A[0][0]*B[0][1] + A[0][1]*B[1][1]
        return C

# Teile A und B in möglichst gleich grosse 4 Teile
# A1: Top Left, A2: Top Right, A3: Bottom Left, A4: Bottom Right
    A1,A2,A3,A4 = divide(A)
    B1,B2,B3,B4 = divide(B)

    print("Teilmatrizen von A:\nA1: ",A1); print("A2: ",A2); print("A3: ",A3); print("A4: ",A4,"\n")
    print("Teilmatrizen von B:\nB1: ",B1); print("B2: ",B2); print("B3: ",B3); print("B4: ",B4,"\n")

# Multiplication of the sub-matrices
# C1: Top Left, C2: Top Right, C3: Bottom Left, C4: Bottom Right
    C1 = Add_Matrices(matMultDC(A1,B1), matMultDC(A2,B3))
    C2 = Add_Matrices(matMultDC(A1,B2), matMultDC(A2,B4))
    C3 = Add_Matrices(matMultDC(A3,B1), matMultDC(A4,B3))
    C4 = Add_Matrices(matMultDC(A3,B2), matMultDC(A4,B4))

    print("Teilergebnisse :\nC1: ",C1); print("C2: ",C2); print("C3: ",C3); print("C4: ",C4,"\n")

# Merging our results (C1,C2,C3,C4) into one Matrix C
# and returning C
    print("Merging results into one Matrix C...")
    C = []
    for k in range(0,len(C1)):
        C.append(C1[k]+C2[k])
    for k in range(0,len(C3)):
        C.append(C3[k]+C4[k])
    printMatrix(C)
    return C


#   TEST

#   (1x1) * (1x1)
#A = [[10]]
#B = [[2]]
#   (1x2) * (2x1)
#A = [[5,3]]
#B = [[10],[1]]
#   (1x4) * (4x1)
#A = [[1,2,1,2]]
#B = [[2],[1],[2],[7]]
#   (1x7) * (7x1)
#A = [[1,2,3,5,9,1,2]]
#B = [[2],[5],[1],[3],[1],[2],[7]]

#   (2x1) * (1x2)
#A = [[2],[1]]
#B = [[1,3]]
#   (3x1) * (1x3)
#A = [[2],[5],[1]]
#B = [[1,2,3]]
#   (5x1) * (1x5)
#A = [[1],[3],[1],[2],[7]]
#B = [[1,5,9,1,2]]
#   (7x1) * (1x7)
#A = [[2],[5],[1],[3],[1],[2],[7]]
#B = [[1,2,3,5,9,1,2]]

#   (2x3) * (3x2)
A = [[3,2,1],[1,0,2]]
B = [[1,2],[0,1],[4,0]]

#   (2x2) * (2x2)
#A = [[1,5],[4,2]]
#B = [[2,3],[4,1]]

#   (3x2) * (2x3)
#A = [[1,0],[4,2],[5,2]]
#B = [[2,1,0],[4,1,3]]

#   (3x3) * (3x3)
#A = [[1,0,3],[4,2,5],[5,2,1]]
#B = [[2,1,0],[4,1,3],[10,1,3]]

#   (4x4) * (4x4)
#A = [[2,3,2,7],[4,5,6,2],[1,0,4,0],[5,3,6,7]]
#B = [[5,8,2,3],[1,0,1,2],[9,3,7,5],[2,6,6,0]]

#   (5x5) * (5x5)
#A = [[1,0,3,1,2],[4,2,5,5,5],[5,2,1,0,0],[1,0,3,1,2],[1,0,3,1,2]]
#B = [[7,3,2,5,1],[4,2,5,1,5],[10,0,1,0,0],[1,0,2,1,2],[1,9,3,1,2]]

#   (3x4) * (4x3)
#A = [[2,3,2,7],[4,5,6,2],[1,0,4,0]]
#B = [[5,8,2],[1,0,1],[9,7,5],[2,6,0]]

#   (4x3) * (3x4)
#A = [[5,8,2],[1,0,1],[9,7,5],[2,6,0]]
#B = [[2,3,2,7],[4,5,6,2],[1,0,4,0]]

#   (4x2) * (2x4)
#A = [[5,8],[1,0],[9,5],[2,0]]
#B = [[2,3,2,7],[4,5,6,2]]

matMultDef(A,B)

print("\nmatMultDC :")
a = matMultDC(A,B)
print("\nBerechnet MatMultDC :")
printMatrix(a)
