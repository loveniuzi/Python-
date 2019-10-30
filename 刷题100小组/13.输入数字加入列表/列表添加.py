#输入数字，将3个偶数加入列表。
lst = []
while len(lst) < 3:
    i = eval(input("请输入一个数字:"))
    if i % 2 ==0:
        lst.append(i)
print(lst)
    
