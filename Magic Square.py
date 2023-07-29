mat = [[17,24,1,8,15],[23,5,7,14,16],[4,6,13,20,22],[10,12,19,21,3],[11,18,25,2,9]]
for i in mat:
    print(i)    
rowsum=0
colsum=0
diagsum1=0
diagsum2=0
for i in range(len(mat)):
    for j in range(len(mat)):
        rowsum = rowsum+mat[i][j]
        colsum = colsum+mat[j][i]
        diagsum1 = diagsum1+mat[i][i]
        diagsum2 = diagsum2+mat[i][len(mat)-i-1]
if(rowsum==colsum==diagsum1==diagsum2):
    print("The given matrix is magic square")
else:
    print("Not a magic square")
