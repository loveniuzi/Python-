# 【问题】生成优秀券号码很多付费应用的开发者，会设计一些优惠券来吸引用户来使用新开发的应用，以达到一定的广告效应。
# 现在，请你帮他们设计并生成200个优惠券号码。优惠码的字符由26个英文字符（大小写）组成，每个优惠码有8位

import string, random

coupons = []                                # coupons表示生成的200个优惠码
for i in range(200):
    list1 = list(string.ascii_letters)      # 从string模块中的ascii_letters表示所有的大小英文字符
    random.shuffle(list1)                   # 打乱列表中的每个字符顺序
    coupon = "".join(list1[0:8])            # 前8个字符连接起来组成一个优惠券coupon
    coupons.append(coupon)                  # 将优惠券加入总的优惠券列表中

print(coupons)                              # 输出200个优惠码
