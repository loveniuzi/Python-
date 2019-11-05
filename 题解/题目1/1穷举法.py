'''
题目描述：
有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
方法：穷举
'''

count = 0       #计数器：满足条件数字的数量    

print("满足条件的数字分别是:")    
                #i j k代表三个位数,i j k中先确定的两位数可以是1-5中任意的只要遍历全部即可
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if( i != k ) and (i != j) and (j != k):
                #输出的顺序决定了i j k分别代表哪一位,可以打乱不影响结果
                print("%d%d%d"%(i, j, k), end = " ")
                count = count + 1
print()
print("满足条件的数字共:%d个"%count)
                
                
