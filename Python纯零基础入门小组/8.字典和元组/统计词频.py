#2. 统计下这段文字里，不同单词出现的次数

sentence = "Beautiful is better than ugly Explicit is better than\
 implicit Simpleis better than complex Complex is better than\
 complicated Flat is better than nested Sparse is better than dense"

wordlist = sentence.split()
wordfrequency = {}

#遍历单词列表，判断是否出现键名
for i in wordlist:
    if i in wordfrequency:
        wordfrequency[i] = wordfrequency[i] + 1
    else:
        wordfrequency[i] = 1

#打印词频字典
print(wordfrequency)
