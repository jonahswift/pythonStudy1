def test1():
    return 443

def test2(num):
    print(num)

result =test1()

#result=test1的返回值
test2(result)
test2(test1())