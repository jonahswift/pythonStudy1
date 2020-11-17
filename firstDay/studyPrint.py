a=5
b=6
print('我今天%d岁了' %a)
print('我今天%d岁了,你今年%d岁了' %(a,b))
print('我今天%03d岁了,你今年%d岁了' %(a,b))

c=a/b
print('%f'%c)
print('%.1f'%c)

age =8
name='Tom'
weight=75.5
student_id=111

print('我的名字是%s' %name)
print('我的学号是%4d' %student_id)
print('我的体重是%.2f公斤' %weight)
print('我的名字是%s,今年我%d岁了' %(name,age))
print('我的名字是%s,明年我%d岁了' %(name,age+1))
#f-格式化字符串
print(f'我的名字是{name},明年{age+1}岁了')

#换行 py中print自带换行
print('换行',end="\n")
print()
print('不换行',end="")
print('不换行',end="")


