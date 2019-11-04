#统计 1 到 100 能被三整除数之和。

sum1 = 0
for i in range(1, 101):
    if i % 3 == 0:
        sum1 = sum1 + i

print("1 到 100 能被三整除数之和:", sum1)
