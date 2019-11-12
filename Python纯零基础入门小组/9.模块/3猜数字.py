import random


answer = random.randint(1, 100)
count = 0

while True:
    guess = int(input("猜一个1到100之间的整数包括100:"))
    count = count + 1
    if guess > answer:
        print("你猜的数字大了")
    elif guess < answer:
        print("你猜的数字小了")
    else:
        print("恭喜你猜对了")
        print("你总共猜了%s次"%count)

        
