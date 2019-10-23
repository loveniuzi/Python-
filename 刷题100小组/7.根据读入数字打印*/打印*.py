#根据读入数字打印 *
#【问题】读取7个数（1—50）的整数值，每读取一个值，程序打印出该值个数的*。

num = 0
for i in range(1, 8):
    num = int(input("输入7个数字,这是第%d个数字:"%i))
    for j in range(num):
        print("*", end = "")
    print()
