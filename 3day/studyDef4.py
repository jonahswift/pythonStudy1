def testA():
    a=100
    print(a)

testA()
#print(a)




a=100 #全局变量
def testA():
    print(a)

def testB():
    a=200#局部变量
    print(a)

testA()
testB()


