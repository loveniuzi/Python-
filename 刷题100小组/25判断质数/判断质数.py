# 【问题】判断输入数字是否为质数
# 【分析】一个大于1的自然数，除了1和它本身外，不能被其他自然数（质数）整除（2, 3, 5, 7等），
# 换句话说就是该数除了1和它本身以外不再有其他的因数.
number = int(input("请输入一个正整数:"))
if number > 1:
    i = 2
    while i != number:
        if (number % i) != 0:
            print(f"{number}不是质数")
            break
        else:
            i = i + 1
    if i == number:
        print(f"{number}是质数")
else:
    print(f"{number}不是质数")
