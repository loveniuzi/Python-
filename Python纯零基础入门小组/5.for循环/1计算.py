#1. 计算100以内所有3的倍数的和
sum1 = 0
for i in range(1, 101):
    if i % 3 == 0:
        sum1 = sum1 + i

print("100以内所有3的倍数的和是:",sum1)
