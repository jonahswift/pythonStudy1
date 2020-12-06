def fn1():
    return 200

print(fn1)
print(fn1())

fn2 =lambda :100
print(fn2)
print(fn2())


def add(a,b):
    return a+b
result =add(2,5)
print(result)

fn3 = lambda a,b:a+b

print(fn3(3,5))