mystr = "hello world and supertest and chaoge and Python"

print('-------------startswith()：检查字符串是否是以指定⼦串开头，是则返回 True，否则返回 False。如果设置开始和结束位置下标，则在指定范围内检查。-----------')

print(mystr.startswith('hello'))
print(mystr.startswith('hel'))
print(mystr.startswith('hello',5,30))

print('--------------endswith()：：检查字符串是否是以指定⼦串结尾，是则返回 True，否则返回 False。如果设置开始和结束位置下标，则在指定范围内检查。---------')
print(mystr.endswith('python'))
print(mystr.endswith('Python'))
print(mystr.endswith('ython'))
print(mystr.endswith('ython',2,22))


print('----------isalpha()：如果字符串⾄少有⼀个字符并且所有字符都是字⺟则返回 True, 否则返回 False。--------')
mystr1='hello'
mystr2='hello123456'
print(mystr1.isalpha())
print(mystr2.isalpha())

print('-----------isdigit()：如果字符串只包含数字则返回 True 否则返回 False。---------')
mystr1='hello123123'
mystr2='123456'
print(mystr1.isdigit())
print(mystr2.isdigit())

print('-----------isalnum()：如果字符串⾄少有⼀个字符并且所有字符都是字⺟或数字则返 回 True,否则返回False。-----')

mystr1 = 'aaa12345'
mystr2 = '12345-'
print(mystr1.isalnum())
print(mystr2.isalnum())

print('----------isspace()：如果字符串中只包含空⽩，则返回 True，否则返回 False。---------')
mystr1 = '1 2 3 4 5'
mystr2 = ' '
print(mystr1.isspace())
print(mystr2.isspace())










