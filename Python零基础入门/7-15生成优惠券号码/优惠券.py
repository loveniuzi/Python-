'''
【问题描述】
很多付费应用的开发者，会设计一些优惠券来吸引用户来使用新开发的应用，以达到一定的广告效应。
现在，请你帮他们设计并生成200个优惠券号码：
优惠码的字符由26个英文字符（大小写）组成
每个优惠码有8位
【解决思路】
list的使用
随机数shuffle
join的使用
字符串处理
'''
import string, random


lst = list(string.ascii_letters)

i = 0
n = int(input("请输入您要产生的优惠券个数:"))
while i < n:
    random.shuffle(lst)
    number = "".join(lst[ :8])
    print(number)
    i = i + 1
