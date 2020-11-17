'''
a=1
if a>0:
    print('a为正数')

print('a的值是',a)
print('---------------------------')
b = -3
if b > 0:
    print('b为正数')

print('b的值是', b)
print('---------------------------')

age =15
if age>18:
    print('年龄已成年，请使用')
print('系统关闭')


print('---------------------------')
age =int(input('请输入你的年龄：'))
if age>=18:
    print(f'年龄为：{age}，年龄通过，请上网！！！')
else:
    print(f'年龄为：{age}，年纪不足，请回家！！！')
print('验证结束')

print('---------------------------')
age = int(input('请输入你的年龄：'))
if age<18:
    print(f'你的年龄为：{age}，年纪不足，不能工作')
elif age>60:
    print(f'你的年龄为：{age}，年纪太大，退休去吧')
elif 18<=age<=60:
    print(f'你的年龄为：{age}，年纪合法，干活去吧')
else:
    print('年纪异常')
print('年纪验证结束')
'''

print('if嵌套---------------------------')
#if嵌套
money =float(input('你是否有钱？'))
if money == True:
    print('可以坐车')
    seat = float(input('车上是否有坐位'))
    if seat == True:
        print('坐着')
    else:
        print('站着')
else:
    print('不能做公交车')














