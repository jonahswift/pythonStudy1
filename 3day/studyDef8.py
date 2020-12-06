def userinfo(*args):
    print(args)

userinfo(3)
userinfo('ddd')
userinfo('ddds',4,'sdsdsd')

list1=[1,2,3,4]
userinfo(list1)#输出字符串
userinfo(*list1)#输出列表类型


def user(**kwargs):
    print(kwargs)

user(name='tom',age=4,id=22212112)
dict1={'name':'jerry','age':43,'id':123212121}
user(**dict1)