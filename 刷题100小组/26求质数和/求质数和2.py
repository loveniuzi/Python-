# 【问题】统计1 到 100 内质数之和
# 利用for else循环奖励机制

sum1 = 0
for num in range(1, 101):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        sum1 = sum1 + num

print(sum1)
