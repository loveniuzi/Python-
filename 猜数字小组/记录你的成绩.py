##统计游戏数据：玩家姓名、总游戏次数（玩家每猜中答案算玩了一次游戏）、
##总游戏轮数（玩家每猜一个数字算玩了一轮游戏）、最快猜中轮数，
##并将结果保存在文件中（请大家本次任务都将数据写入 game_one_user.txt ）

import random

# min_count表示最快猜中的轮数,times表示总游戏次数
min_count = 100
times = 0
playAgain = 'y'

while playAgain == 'y':
    name = input("请输入你的姓名:")
    secret = random.randint(1, 100) 
    count = 0
    guess = 101                                         # count表示猜了几次猜对了
    while secret != guess:
        guess = int(input("请猜一个1到100之间的整数:"))
        count = count + 1
        if guess > secret:
            print("你猜的数字大了")
        elif guess < secret:
            print("你猜的数字小了")
        else:
            print(f"恭喜你！猜对了数字是:{secret},你一共猜了{count}次。")
            times = times + 1
            if count < min_count:
                min_count = count
            playAgain = input("你是否还要继续游戏?(继续输入y)").lower()
            
    file = open("game_one_user.txt", "w")
    file.write(f"{name} {str(times)} {str(min_count)}")
    file.close()

