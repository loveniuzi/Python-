# 一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？

import math

num = -100
while True:
    if math.sqrt(num + 100).is_integer() and math.sqrt(num + 268).is_integer():
        print(f"这个整数是{num}")
    num = num + 1

