print('-------创建集合使⽤ {} 或 set() ， 但是如果要创建空集合只能使⽤ set() ，因为 {} ⽤来创建空字典。---------------')
s1={10,20,30,40,50}
print(s1)

s2={10,20,30,40,50,30,40,50,}#集合自动去重、无序
print(s2)

s3=set('qweew')
print(s3)

s4 =set()   #集合类型
print(type(s4))

s5={}   #字典类型
print(type(s5))

print('------------add()当向集合内追加的数据是当前集合已有数据的话，则不进⾏任何操作。----------')
s1={100,200}
s1.add(100)
s1.add(111)
print(s1)

print('-----------update(), 追加的数据是序列。-----------')
s1={100,200}
#s1.update(125)  TypeError: 'int' object is not iterable
s1.update([100,200,300])
s1.update('sdsdd')
print(s1)

print('------------remove()，删除集合中的指定数据，如果数据不存在则报错。----------')
s1 = {10, 20}
s1.remove(10)
print(s1)

#s1.remove(10)   KeyError: 10 数据不存在则报错

print('---------discard()，删除集合中的指定数据，如果数据不存在也不会报错。-------------')
s1 = {10, 20}
s1.discard(10)
print(s1)
s1.discard(10)
print(s1)

print('---------pop()，随机删除集合中的某个数据，并返回这个数据。-------------')
s1 = {10, 20, 30, 40, 51, 40}
delNum=s1.pop()
print(delNum)
print(s1)

fruits = {"apple", "banana", "cherry"}

x = fruits.pop()
print(fruits)

print(x)

print('---------in：判断数据在集合序列-------------')
s1 = {10, 20, 30, 40, 50}
print(10 in s1)
print(13 in s1)

print('----------not in：判断数据不在集合序列------------')
s1 = {10, 20, 30, 40, 50}
print(10 not in s1)
print(13 not in s1)