#【问题】实际判断闰年，输出2月的天数
#【分析】百年除以400，非百年除以4，能除尽则为闰年


# 定义判断闰年的函数
def leap_year(year):
    # 判断是否是百年
    if year % 100 == 0:
        if year % 400 == 0:
            print(year)
    else:
        if year % 4 == 0:
            print(year)


for i in range(1000, 2001):
    leap_year(i)
