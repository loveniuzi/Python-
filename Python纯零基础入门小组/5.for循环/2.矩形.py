#2. 分别输入高和宽两个整数，输出对应高度和宽度的矩形。比如：
#输入3和4，输出
#      * * * *
#      * * * *
#      * * * *

h = int(input("请输入高度:"))
w = int(input("请输入宽度:"))

for i in range(0, h):
    for j in range(0, w):
        print("*", end = " ")
    print()
