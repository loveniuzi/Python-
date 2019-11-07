'''
【问题】输入数字，如果平方运算后小于 50 则退出。
'''

# 请求输入
number = float(input("请输入一个数字:"))

# 判断
while (number ** 2) >= 50:
    number = float(input("请输入一个数字:"))
print("输入结束")
