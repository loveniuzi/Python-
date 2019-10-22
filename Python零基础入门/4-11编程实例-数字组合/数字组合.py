#1,2,3,4 四个数字，能组成多少个互不相同且无重复数字的三位数？分别是多少？
#要求：输出 1,2,3,4 组合出的所有无重复数字的三位数。
for i in range(1, 5):
    for j in range(1, 5):
        if i != j:
            for k in range(1, 5):
                if (k != j) and (k != i):
                    print("%d%d%d"%(i, j, k))
