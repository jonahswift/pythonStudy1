num =1
print(num)

num1,float1,str1 = 10,0.5,'hello'
print(num1)
print(float1)
print(str1)

a=b=10
print(a)
print(b)

print('-------------')

a=100
a +=20
print(a)

b=2
b *=3
print(b)

c=10
c +=3 +5
print(c)

print('------------------')

a=7
b=5
print(a==b)
print(a !=b)
print(a<b)
print(a>b)
print(a<=b)
print(a>=b)
print('----------------')

a=1
b=2
c =3
print(a<b and b<c)
print((a>b)and (b<c))
print(a>b or  b<c)
print(not a>b)
print('----------------')

#and运算 只要一个为0，结果为0，否则为最后一个非0的结果
a,b,c=0,1,2
print(a and b)
print(b and a)
print(a and c)
print(c and a)
print(b and c)
print(c and b)
print('----------------')
#or运算，所有值为0时才为0，否则为第一个非0的数字
print(a or b)
print(a or c)
print(b or c)
d=0
print(a or d)
