##【问题】打印图形用符号的组合在控制台输出不同大小的矩形图案。
##要求：写一个输出矩形的函数，该函数拥有三个默认参数，矩形的长5、宽5和组成图形的点的符号“*”，
##为函数添加不同的参数，输出三个不同类型的矩形

def draw_rect(symbol = '*', long = 5, width = 5):
    for i in range(width):
        for j in range(long):
            print(symbol, end = "")
        print()


draw_rect()
