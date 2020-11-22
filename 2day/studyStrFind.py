str1=" Hi man,what's up. hi I'm OK "
#find 区分大小写
print(str1.find('hi'))

str2=" hello  man,what's up. hello I'm OK "
print(str2.find('hello'))
print(str2.find('hello',10,30))
print(str2.find('Hello'))  #不存在返回-1


print('1111')