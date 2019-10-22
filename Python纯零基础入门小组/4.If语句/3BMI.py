#BMI 指数（即身体质量指数，简称体质指数又称体重，英文为Body Mass Index，简称BMI），是用体重公斤数除以身高米数平方得出的数字
#BMI < 18.5 体重偏轻
#18.5 <= BMI < 24 体重正常
#BMI >= 24 体重偏重
#设计一个BMI计算器吧，看看自己体重是否正常。
#输入：身高、体重值
#输出：BMI 指数、是否正常

height = eval(input("请输入你的身高值（以米为单位）:"))
print("你的身高为",height,"米")
weight = eval(input("请输入你的体重值（以公斤为单位）:"))
print("你的体重为",weight,"公斤")

bmi = weight / (height ** 2)
print("你的BMI值为:%s"%bmi)

if bmi < 18.5:
    print("你的体重偏轻。")
elif bmi < 24:
    print("你的体重正常。")
else:
    print("你的体重偏重。")
