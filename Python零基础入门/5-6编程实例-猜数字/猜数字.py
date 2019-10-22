#有一个猜数字的游戏：程序随机一个结果，用户通过命令行输入去猜。程序会告诉你猜大了还是小了，直到猜中为止。
#现在，请你独立实现这个小游戏，并且加上一些功能，比如：
#游戏可以反复进行，猜中了之后可以重新开始
#统计用户猜了几轮，平均几次猜中
#限制每轮猜的次数，判定输赢
import random


answer = random.randint(0, 9)
count = 0

while True:
    if count > 4:
        break
    guess = int(input("猜一个0到9之间的整数包括9(你有5次机会):"))
    count = count + 1
    if guess > answer:
        print("你猜的数字大了")
    elif guess < answer:
        print("你猜的数字小了")
    else:
        print("恭喜你猜对了")
        print("你总共猜了%s次"%count)
        answer = random.randint(0, 9)
        
print("抱歉！你的机会已经用光！")

        
