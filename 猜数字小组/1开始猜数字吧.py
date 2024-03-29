# 任务
# 提示用户猜一个数字，把 用户输入的数字A 与 一个程序随机生成的数字B 进行比较，
# 提示 数字A 大于/小于/等于 数字B。用户可以反复猜 数字B，直到猜中为止
##1. 使用模块 random，生成 1-100 之间的一个随机数并赋值给 变量A，作为之后要猜的数字；
##2. 使用 input 函数提示用户输入一个数字，将用户输入的字符串类型的内容使用 int() 函数转换成数字类型并赋值给 变量B；
##3. 将 变量B 与 变量A 进行比较，用 if, elif, else 语句判断大小，并输出猜的数字大于/小于/等于 变量A；
##4.  将步骤 2 和 3 中实现的代码放入 while 循环中，使得用户可以反复猜数字（注意要将程序生成的随机数放在循环外面，避免每次循环内部都重新生成随机数）；
##5. 当猜中后，退出 while 循环；

import random

secret = random.randint(1, 100)
n = 0
while True:
    guess = int(input("请猜一个1到100之间的整数:"))
    n = n + 1
    if guess > secret:
        print("你猜的数字大了")
    elif guess < secret:
        print("你猜的数字小了")
    else:
        print(f"恭喜你！猜对了数字是:{secret},你一共猜了{n}次。")
