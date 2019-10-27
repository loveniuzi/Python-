'''
【问题】请使用 * 打印出如下
* * * * *
*     *
*   *
* *
*
'''

for i in range(5):
    for j in range(5):
        if j == 0 or (4 - j) == i or i == 0:    #行号为0或列号为0以及斜着都打印*
            print('*', end = ' ')
        else:
            print(' ', end = ' ')
    print()
