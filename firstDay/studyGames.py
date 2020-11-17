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
#num = random.randint(1,3)
#print(num)

puit = str(input('请猜拳：'))
num = random.randint(1,3)
'''
if num == 1:
    a ='石头'
   print(f'电脑出的是{a}')
elif num==2:
    a = '剪子'
   # print(f'电脑出的是{a}')
else:
    a = '布'
    #print(f'电脑出的是{a}')
#print(f'电脑出的是{num}')
'''

if (puit == '石头' and num == 1)or(puit == '剪子' and num == 2)or(puit == '布' and num == 3):
    print(f'你出的{puit},电脑出的{num},打平了')
elif (puit == '石头' and num == 2)or(puit == '剪子' and num == 3)or(puit == '布' and num == 1):
    print(f'你出的{puit},电脑出的{num},你赢了')
else:
    print(f'你出的{puit},电脑出的{num},你输了')



