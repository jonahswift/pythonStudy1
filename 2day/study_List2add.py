

print('------------append()：列表结尾追加数据。-----------')
name_list = ['Tom', 'Lily', 'Rose']
name_list.append('ahua')
print(name_list)

print('---------------如果append()追加的数据是⼀个序列，则追加整个序列到列表---------------')
name_list = ['Tom', 'Lily', 'Rose']
name_list.append(['ahua','tangtang'])
print(name_list)

print('-----------extend()：列表结尾追加数据，如果数据是⼀个序列，则将这个序列的数据逐⼀添加到列表---------------')
name_list = ['Tom', 'Lily', 'Rose']
name_list.extend('huahau')
print(name_list)

name_list.extend(['huahau'])
print(name_list)

print('------------extend()序列数据------------')
name_list = ['Tom', 'Lily', 'Rose']
name_list.extend(['hauhau','jaijai'])
print(name_list)

print('----------insert()：指定位置新增数据。---------')
name_list = ['Tom', 'Lily', 'Rose']
name_list.insert(1,'haha')
print(name_list)

name_list.insert(1,['haha','jiji'])
print(name_list)

