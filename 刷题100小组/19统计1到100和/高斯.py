'''
【问题】利用高斯算法统计 1 到 100 之和，以首项加末项乘以项数除以2
用来计算“1+2+3+4+5+···+（n-1）+n”的结果。这样的算法被称为高斯算法。
'''


list1 = list(range(1, 101))
list2 = list1[ : :-1]
sum1 = 0

# 求和
for i in range(0, 100):
    sum1 = sum1 + list1[i] + list2[i]

# 输出结果
sum1 = sum1 / 2
print("1到100的和为:%d"%sum1)
