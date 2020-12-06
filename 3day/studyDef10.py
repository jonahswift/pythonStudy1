a=1
b=a
print(b)
print(id(a))
print(id(b))

a=2
print(b)
print(id(a))#a被重新定义了一个新的内存中
print(id(b))


aa=[10,20]
bb=aa

print(id(aa))
print(id(bb))

aa.append('30')  #修改了aa，bb所指定的内存  所以aa，bb都指向了新的内存中
print(bb)

print(id(aa))
print(id(bb))



print('---------------------')

def test1(a):
    print(a)
    print(id(a))

    a+=a
    print(a)
    print(id(a))

b=100
test1(b) #int类型a被重新指向内存

c=[11,22]
test1(c) #列表 修改了指定的内存，a使用的内存地址没有变化