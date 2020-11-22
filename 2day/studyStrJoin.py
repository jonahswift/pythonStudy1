list1 = ['chao', 'ge', 'test', 'promotion']
t1 = ('aa', 'b', 'cc', 'ddd')

print('_'.join(list1))
print(' '.join(list1))
print(''.join(t1))
print(''.join(list1))


print('-------------------------capitalize---------------------------------')



mystr = "hello world and supertest and chaoge and Python"
#capitalize()：将字符串第⼀个字符转换成⼤写,其他全小写。
print(mystr.capitalize())

print('-------------------------title：将字符串每个单词⾸字⺟转换成⼤写。---------------------------------')
print(mystr.title())

print('-------------------------lower()：将字符串中⼤写转⼩写。---------------------------------')
print(mystr.lower())

print('-------------------------upper()：将字符串中⼩写转⼤写。---------------------------------')
print(mystr.upper())



mystr1 = "      hello world and supertest and chaoge and Python    "

print('-------------------------lstrip()：删除字符串左侧空⽩字符。---------------------------------')
print(mystr1.lstrip() + 'test')


print('-------------------------rstrip()：删除字符串右侧空⽩字符。---------------------------------')
print(mystr1.rstrip() + 'test')

print('-------------------------strip()：删除字符串两侧空⽩字符。---------------------------------')
print(mystr1.strip() + 'test')

mystr2='hello'
print('-------------------------ljust()：返回⼀个原字符串左对⻬,并使⽤指定字符(默认空格)填充⾄对应⻓度 的新字符串。---------------------------------')
print(mystr2.ljust(10,'.'))

print('-------------------------rjust()：返回⼀个原字符串右对⻬,并使⽤指定字符(默认空格)填充⾄对应⻓度 的新字符串，语法和ljust()相同。---------------------------------')
print(mystr2.rjust(10,'.'))

print('-------------------------center()：返回⼀个原字符串居中对⻬,并使⽤指定字符(默认空格)填充⾄对应⻓度 的新字符串，语法和ljust()相同。---------------------------------')
print(mystr2.center(10,'.'))








