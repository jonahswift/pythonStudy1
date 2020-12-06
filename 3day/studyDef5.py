glo_mun=0 #全局变量

def test1():
    global glo_mun
    #修改全局变量
    glo_mun=100

def test2():
    print(glo_mun)

#打印全局变量
test2()
#修改全局变量
test1()
#打印修改后的全局变量
test2()