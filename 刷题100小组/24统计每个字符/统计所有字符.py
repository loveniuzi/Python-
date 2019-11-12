# 【问题】从控制台输入一段字符，统计字符出现次数

st = input("请输入一段字符:")
dic = {}
for ch in st:
    if ch in dic:
        dic[ch] = dic[ch] + 1
    else:
        dic[ch] = 1
print(dic)
