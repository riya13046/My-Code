row=int(input())
mat=[]
out=[]
for i in range(row):
    mat.append(list(map(int,input().split())))
col=len(mat[0])
#to check consecutive 3 elements in row
for r in range(row):
    for c in range(col-2):
        if mat[r][c]==mat[r][c+1]==mat[r][c+2]:
            out.append(mat[r][c])
#to check in column
for r in range(row-2):
    for c in range(col):
        if mat[r][c]==mat[r+1][c]==mat[r+2][c]:
            out.append(mat[r][c])
# to check in diagonal
for r in range(row-2):
    for c in range(col-2):
        if mat[r][c]==mat[r+1][c+1]==mat[r+2][c+2]:
            out.append(mat[r][c])
print(out)
# to print min in case of multipe numbers  
print(min(out))
            
