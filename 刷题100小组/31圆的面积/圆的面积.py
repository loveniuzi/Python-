# 【问题】输入圆的半径求计算圆的面积，pi = 3.142
# 【分析】圆的面积公式: pi*r*r

r = float(input("请输入圆的半径:"))
pi = 3.142
area = pi * r ** 2 
print(f"半径为{r}的圆的面积为{area}")
