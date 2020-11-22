print('--------定义元组---------')
#如果定义的元组只有⼀个数据，那么这个数据后⾯也好添加逗号，否则数据类型为唯⼀的这个数据的数据类型
t1=(10,10,20)
t2=(10,)

print('---------按下标查找数据--------')
tuple1 = ('aa', 'bb', 'cc', 'bb')
print(tuple1[1])

print('-------index()：查找某个数据，如果数据存在返回对应的下标，否则报错----------')
tuple1 = ('aa', 'bb', 'cc', 'bb')
print(tuple1.index('aa'))
#print(tuple1.index('cc1')) 不存在提示ValueError: tuple.index(x): x not in tuple

print('----------count()：统计某个数据在当前元组出现的次数。-------')
tuple1 = ('aa', 'bb', 'cc', 'bb','cc')
print(tuple1.count('cc'))

print('---------len()：统计元组中数据的个数。--------')
tuple1 = ('aa', 'bb', 'cc', 'bb','cc')
print(len(tuple1))

print('--------1、元组内的直接数据如果修改则⽴即报错2、如果元组⾥⾯有列表，修改列表⾥⾯的数据则是⽀持的---------')

tuple1 = ('aa', 'bb', 'cc', 'bb')
#tuple1[0]='aaa'    'tuple' object does not support item assignment

tuple2 = (10, 20, ['aa', 'bb', 'cc'], 50, 30)
print(tuple2)
tuple2[2][1] ='bbbbbbb' #元组内的list列表支持修改
print(tuple2)
