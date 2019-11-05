'''
题目描述：
有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
方法：排列组合
'''

    #全排函数定义
def arrangement(n):
    #保存计算结果
    result = 1
    #不为0时进行累乘计算
    if  n < 0:
        print("error")
    elif n == 0:
        pass
    else:
        for i in range(1, n + 1):
            result = result * i
    #返回计算结果
    return result

    #组合函数定义
def combination(n, k):
    if k < 0 or k > n:
        print("error")
    else:
        x = arrangement(n) 
        y = arrangement(k) * arrangement(n - k)
        #返回计算结果
        return int(x / y)
