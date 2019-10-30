#【问题】输入整数，判断是否为偶数，是则加入列表，列表满三个元素则程序退出并按从小到大顺序输出。
lst = []
while len(lst) < 3:
    i = eval(input("请输入一个数字:"))
    if i % 2 ==0:
        lst.append(i)
lst.sort()
print(lst)
    
