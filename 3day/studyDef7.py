def userInfo(name,age,gender):
    print(f'你的名字是：{name}，年龄是：{age}，性别是：{gender}')

userInfo('rose',22,'女')
userInfo('小米',gender='男',age=51)



def chengji(name1,banji,chengji=22):
    print(f'名字为{name1},班级为:{banji},成绩为：{chengji}')

chengji('jiji',2)
chengji('dd','ff')