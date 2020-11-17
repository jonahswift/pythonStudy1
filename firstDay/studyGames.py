'''
需求：游戏 石头剪刀 布
分析：
玩家：a
电脑：b

剪子：1 布：2    石头3

输赢
玩家：剪子 电脑 布
a==1 and b==2
'''
import random
#随机数
num = random.randint(1,3)
print(num)