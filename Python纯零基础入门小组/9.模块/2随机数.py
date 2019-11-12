# 生成10个随机数，输出里面最大的数

import random

l = []
for i in range(10):
    ran = random.randint(1, 100)
    l.append(ran)
print(f"您生成的随机数是{l},其中最大的数是{max(l)}")
