#【问题】判断闰年
#【分析】百年除以400，非百年除以4，能除尽则为闰年

year = int(input("请输入年份:"))

# 判断是否是百年
if year % 100 == 0:
    if year % 400 == 0:
        print(f"{year}年是世纪闰年。")
    else:
        print(f"{year}年不是闰年。")
else:
    if year % 4 == 0:
        print(f"{year}年是普通闰年。")
    else:
        print(f"{year}年不是闰年。")
