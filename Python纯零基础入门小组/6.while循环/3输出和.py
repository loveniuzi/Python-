# 使用 while 计算100以内所有3的倍数的和
count = 0
sum1 = 0
while count < 100:
    count += 1
    if count % 3 == 0:
        sum1 = sum1 + count

print("100以内所有3的倍数的和:",sum1)
