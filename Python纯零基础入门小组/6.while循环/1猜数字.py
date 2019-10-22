import random


answer = random.randint(0, 9)
count = 0
result = False

while result == False:
    guess = int(input("猜一个0到9之间的整数包括9:"))
    count = count + 1
    if guess > answer:
        print("你猜的数字大了")
        result == False
    elif guess < answer:
        print("你猜的数字小了")
        result == False
    else:
        print("恭喜你猜对了")
        print("你总共猜了%s次"%count)
        result = True
