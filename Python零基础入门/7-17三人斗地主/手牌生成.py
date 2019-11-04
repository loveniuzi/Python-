'''
【问题描述】
三人斗地主手牌规则：
一副牌 54 张（4 种花色各 13 张，大小王），一人 17 张，留 3 张做底牌。
要求：
将一副牌随机打乱（洗牌）后分配给 3 位玩家（发牌），输出每个人的手牌和剩余底牌。
可使用 list 和 random 完成。
【解决思路】
通过两个 list 或 tuple，一个表示花色，一个表示点数，循环生成 52 张牌。再添加上大小王，保存在列表中。
使用 random.shuffle 将列表顺序打乱。
按顺序轮流发牌，可直接输出，也可以保存在列表中，最后一起输出。
另一种方法：也可以使用 random.choice 从列表中随机取牌，然后从列表中移除已被选中的牌。
'''
import random


#S_方块,P_梅花,B_黑桃,R_红桃
lst1 = ["S_", "P_", "B_", "R_"]
lst2 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K",]
lst = []

for l1 in lst1:
    for l2 in lst2:
        lst.append(l1+l2)
lst.extend(["Big_King", "Small_King"])

random.shuffle(lst)
name1 = lst[0: :3]
name2 = lst[1: :3]
name3 = lst[2: :3]
recards = lst[-3: :1]

print("玩家1的牌是:",name1)
print("玩家2的牌是:",name2)
print("玩家3的牌是:",name3)
print("底牌是:",recards)
