#1字符串拼接
name = "Crossin"
age = 18
code = "Python"
# 通过 % 将 name, age, code 拼接成一句话
# 输出 Crossin is 18, he writes Python.
result = name + "is " + str(age) + " " + code
print(result)


#2print()
num1 = '3.3'
num2 = 2.5
# 将 num1 转换为浮点数
num1 = float(num1)
# 再和 num2 相加后输出
print(num1 + num2)


#3bool类型转换
print("bool(-123)", bool(-123))
print("bool(0)", bool(0))
print("bool('abc')", bool('abc'))
print("bool('False')", bool('False'))
print("bool('')", bool(''))
print("bool([])", bool([]))
print("bool({})", bool({}))
print("bool([''])", bool(['']))
print("bool(None)", bool(None))
