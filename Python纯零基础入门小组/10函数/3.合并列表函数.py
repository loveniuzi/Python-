# 3. 实现一个函数，输入参数是两个列表，输出返回值是两个列表元素合并并排序后的结果，
# 比如 combine([1,5,3], [2,6,7,4])
# 返回结果[1,2,3,4,5,6,7]

def combine(list1 = [], list2 = []):
    list1.extend(list2)
    list1.sort()
    return list1

print(combine([1,5,3], [2,6,7,4]))
