#【问题】输入3个整数a,b,c，按大小顺序输出。
lst = []
for i in range(3):
    lst.append(int(input("输入整数：")))
print("你输入的三个整数是", lst)
lst.sort()
print("按大小顺序排列为", lst)
