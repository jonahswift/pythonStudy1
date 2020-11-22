
print('--------删除列表-------')
name_list = ['Tom', 'Lily', 'Rose']
del name_list
#print(name_list)

print('----------删除指定数据-------------------')
name_list = ['Tom', 'Lily', 'Rose']
del name_list[1]
print(name_list)

print('-------------pop()：删除指定下标的数据(默认为最后⼀个)，并返回该数据。----------------')
name_list = ['Tom', 'Lily', 'Rose']
del_list=name_list.pop(1)
print(del_list)
print(name_list)

print('-------------remove()：移除列表中某个数据的第⼀个匹配项。----------------')
name_list = ['Tom', 'Lily', 'Rose']
name_list.remove('Rose')
print(name_list)


#name_list.remove('bucunzai') 删除不存在的会报错
print(name_list)

print('-------------clear()：清空列表----------------')
name_list = ['Tom', 'Lily', 'Rose']
name_list.clear()
print(name_list)


