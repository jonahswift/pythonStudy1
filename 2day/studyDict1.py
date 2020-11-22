print('------字典的语法---------')
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
# 空字典
dict2 = {}
dict3 = dict()

print('-----------增 如果key存在则修改这个key对应的值；如果key不存在则新增此键值对。------------')
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
dict1['name']= 'rose'
print(dict1)
dict1['id'] ='21321231'
print(dict1)

print('----------del() / del：删除字典或删除字典中指定键值对。-------------')
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
del dict1['name']
print(dict1)

print('-----------clear()：清空字典------------')
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
dict1.clear()
print(dict1)

print('-----------改写法：字典序列[key] = 值 和新增一样------------')
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
dict1['name']='sss'
print(dict1)

print('------------key值查找-----------')
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
print(dict1['name'])
#print(dict1['id'])  KeyError: 'id'   key值查找不存在就报错

print('---------get() 字典序列.get(key, 默认值)--------------')
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
print(dict1.get('name'))
print(dict1.get('id')) #不存在时默认返回None
print(dict1.get('id','不存在')) #不存在时可定义默认返回

print('----------keys() values()返回key、values列表-------------')
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
print(dict1.keys())
print(dict1.values())

print('----------items() 安列表返回字典，keys+values组合-------------')
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
print(dict1.items())

print('--------for遍历字典的key、value--------')
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
for i in dict1.keys():
    print(i)

print('----------------')

for i in dict1.values():
    print(i)

print('---------遍历字典的元素-------')
for i in dict1.items():
    print(i)

print('---------遍历字典的键值对-------')
for k,v in dict1.items():
    print(f'key为：{k},value为：{v}')
