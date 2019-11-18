# 【问题】统计1 到 100 内质数之和

def is_prime(num):
    i = 2
    while i < num and i != 1:
        if num % i == 0:
            break
        else:
            i = i + 1
    if i == num:
        return num
    else:
        return 0

sumnum = 0
for num1 in range(1, 101):
    sumnum = sumnum + is_prime(num1)

print(f"1到100内质数之和为:{sumnum}")
