'''
num = input('请输入一个数字：')
print(f'您输入的数字是：{num}')
print(type(num))
#转换为int
print(type(int(num)))
'''
#1\、转换为浮点型float
num1 =1
print(float(num1))
print(type(float(num1)))

#2、转换为字符串str
num2=20
print(str(num2))
print(type(str(num2)))

#3转换为元组类型
list1 = [10,20,30]
print(list(list1))
print(type(list(list1)))
print('----')
#4转换为列表类型
t1 =(100,200,300)
print(tuple(t1))
print(type(tuple(t1)))
print('----')
#5类型还原
str1 ='10'
str2 ='[1,2,3]'
str3 = '(100,200,300)'
print(type(eval(str1)))
print(type(eval(str2)))
print(type(eval(str3)))
