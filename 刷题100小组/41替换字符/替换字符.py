# 【问题】使用 * 替换字符串‘你好，我好，大家好才是真的好！’中的‘好’。

string = "你好，我好，大家好才是真的好！"
string1 = ""

for ch in string:
    if ch == "好":
        string1 = string1 + "*"
    else:
        string1 = string1 + ch
        
print(string1)
