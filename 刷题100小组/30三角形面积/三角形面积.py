# 输入三角形三个边求计算三角形的面积
#【问题】输入三角形三个边求计算三角形的面积
#【分析】"三角形两边之和大于第三边，S=sqrt[p(p-a)(p-b)(p-c)]"


import math

triangle = []
for i in range(1, 4):
    side = float(input(f"请输入三角形第{i}条边的长度:"))
    triangle.append(side)
triangle.sort()

a, b, c = triangle
if (a + b) > c:
    p = (a + b + c) / 2
    area = math.sqrt(p*(p-a)*(p-b)*(p-c))
    print(f"您输入的三角形面积为:{area}")
else:
    print("您输入有误！")
