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

puit = str(input('请猜拳，你出了：'))
num = random.randint(1,3)


#print(f'电脑出的是{num}')


if num ==1:
    num1 = '石头'
elif num ==2:
    num1 = '剪子'
else:
    num1 ='布'
print(f'电脑出的是{num1}')

if (puit == '石头' and num == 1)or(puit == '剪子' and num == 2)or(puit == '布' and num == 3):
    print(f'你出的{puit},电脑出的{num1},打平了')
elif (puit == '石头' and num == 2)or(puit == '剪子' and num == 3)or(puit == '布' and num == 1):
    print(f'你出的{puit},电脑出的{num1},你赢了')
else:
    print(f'你出的{puit},电脑出的{num1},你输了')



