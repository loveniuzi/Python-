# 1 x 1 = 1
# 1 x 2 = 2
# ...
# 9 x 1 = 9
# ...
# 9 x 9 = 81

for i in range(1, 10):
    for j in range(1, 10):
        print('%d x %d = %d' % (i, j, i * j))
