# 【问题】输入一行字符，如'are you ok ! 黎明。'。
# 分别统计出其中英文字母、空格、数字和其它字符的个数。

import string


en_ch = 0
ch_ch = 0
num_ch = 0
blank = 0
others = 0

strings = input("请输入一行字符:")
for c in strings:
    if c in string.ascii_letters:
        en_ch = en_ch + 1
    elif c.isalpha():
        ch_ch = ch_ch + 1
    elif c.isspace():
        blank = blank + 1
    elif c.isdigit():
        num_ch = num_ch + 1
    else:
        others = others + 1

print(f"您输入的内容中英文字符有{en_ch}个。")
print(f"您输入的内容中中文字符有{ch_ch}个。")
print(f"您输入的内容中数字字符有{num_ch}个。")
print(f"您输入的内容中空格有{blank}个。")
print(f"您输入的内容中其它字符有{others}个。")
