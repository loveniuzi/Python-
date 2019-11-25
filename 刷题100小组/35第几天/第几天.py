def isleap(year):
    if year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    else:
        if year % 4 == 0:
            return True
        else:
            return False


y = int(input("请输入年:"))
m = int(input("请输入月:"))
d = int(input("请输入日:"))
days1 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days2 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = 0

if m > 1:
    if isleap(y):
        days = sum(days1[0:m-1]) + d
    else:
        days = sum(days2[0:m-1]) + d
else:
    days = d
print(f"{y}年{m}月{d}日是这一年的第{days}天")
