##程序在用户猜中答案后，输出猜中答案一共猜了多少轮（用户每输入一次计做一轮），
##并可以反复进行游戏（用户猜中一次后可选择“继续”还是“退出”）

import random

secret = random.randint(1, 100)
playAgain = 'y'

while playAgain == 'y':
    guess = int(input("请猜一个1到100之间的整数:"))
    count = 1
    while secret != guess:
        guess = int(input("请猜一个1到100之间的整数:"))
        count = count + 1
        if guess > secret:
            print("你猜的数字大了")
        elif guess < secret:
            print("你猜的数字小了")
        else:
            print(f"恭喜你！猜对了数字是:{secret},你一共猜了{count}次。")
            playAgain = input("你是否还要继续游戏?(继续输入y)").lower()
