## 【问题】两个 3 行 3 列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵：
## X = [[12,7,3],
##     [4 ,5,6],
##     [7 ,8,9]] 
## Y = [[5,8,1],
##     [6,7,3],
##     [4,5,9]]


X = [[12,7,3],
     [4 ,5,6],
     [7 ,8,9]]
Y = [[5,8,1],
     [6,7,3],
     [4,5,9]]
Z = [[0, 0, 0]] * 3

for i in range(3):
    for j in range(3):
        Z[i][j] = X[i][j] + Y[i][j]
print(Z)
