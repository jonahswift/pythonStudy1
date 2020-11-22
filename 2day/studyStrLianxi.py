#输入一个名字，判断是班级里否有人 如果有 是否重名   有，输出重名个数  否提示无重名
#不在，则提示不在
'''
banjimingdan='' xiesheng zhanghao meiya xiaoxin xiaoxin''
name=input('请输入查询的名称')

find = banjimingdan.find(name)
if find == -1:
    print('此人不在班级中')
else:
    print('班级中有这个人')
    num = banjimingdan.count(name)
    if num==1:
        print()

    else:
        print(f'班级中重名有{num}个人')

'''

banjimingdan=' xiesheng zhanghao meiya xiaoxin xiaoxin '
name=input('请输入查询的名称')
find=banjimingdan.count(name)
if find==0:
    print('此人不在班级中')
elif find ==1:
    print('班级中有这个人，无重名')
else:
    print(f'班级中重名有{find-1}个人')
