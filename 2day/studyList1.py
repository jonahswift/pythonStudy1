name_list = ['tom','jerry','rose']

print('------------下标----------')
print(name_list[0])
print(name_list[1])
print(name_list[2])

print('----------index()：返回指定数据所在位置的下标 。不存在则报错-------------')
print(name_list.index('tom'))

print('------------------count()：统计指定数据在当前列表中出现的次数。---------------')

print(name_list.count('tom'))

print('----------len()：访问列表⻓度，即列表中数据的个数。-------------')

print(len(name_list))

print('-----------in：判断指定数据在某个列表序列，如果在返回True，否则返回False-----------')

print('tom' in name_list)
print('jettyy' in name_list)

print('--------------not in：判断指定数据不在某个列表序列，如果不在返回True，否则返回False-----------')
print('tom' not in name_list)
print('tomme' not in name_list)

print('-------查找⽤户输⼊的名字是否已经存在。----')
name_list = ['tom','jerry','rose','tom']
name = input('请输入姓名')
if name in name_list:
    print('你在该班级中')
    if name_list.count(name)==1:
        print()
    else:
        print(f'你的名字重复了，重复了{name_list.count(name)-1}次')
else:
    print('你不在该班级中')

