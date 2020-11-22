print('创建⼀个0-10的列表。')
print('--------------while循环实现-------------------')
list1=[]
i=0
while i<=10:
    list1.append(i)
    i+=1
print(list1)

print('---------------for循环实现------------------')
list1=[]
for i in range(10+1):
    list1.append(i)

print(list1)

print('-----------------列表推导式实现----------------')
list2 = [i for i in range(10+1)]
print(list2)

print('需求：创建0-10的偶数列表')
print('-----------带if的列表推导式----------------------')
list1 = [i for i in range(0,33,2)]
print(list1)

list1=[i for i in range(20) if i%2 == 0]
print(list1)

print('-------------多个for循环实现列表推导式--------------------')
#[(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
list1=[(i,j) for i in range (1,3) for j in range (3)]
print(list1)


list1=[(i,j) for i in range (1,10) if i%2 ==0 for j in range (3)]
print(list1)

print('--------------字典推导式-------------------')
print('----------------字典key是1-5数字，value是这个数字的2次⽅。-----------------')
#字典key是1-5数字，value是这个数字的2次⽅。
dict1 ={i:i**2 for i in range(1,5)}
print(dict1)

i=0
dict1={}
for i in range(1,5):
    dict1[i]=i**2
    i+=1
print(dict1)

print('----------------将两个列表合并为⼀个字典-----------------')
list1 = ['name', 'age', 'gender']
list2 = ['Tom', 20, 'man']
dict1 ={list1[i]:list2[i] for i in range(len(list1))}
print(dict1)

print('------------------提取字典中⽬标数据---------------')
counts = {'MBP': 268, 'HP': 125, 'DELL': 201, 'Lenovo': 199, 'acer': 99}
count1={key:value for key,value in counts.items() if value>=200}
print(count1)


print('-------------创建⼀个集合，数据为下⽅列表的2次⽅--------------------')
list1 = [1, 1, 2,3]
set1 ={i **2 for i in list1}
print(set1)
print('---------------------------------')

