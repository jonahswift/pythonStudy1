import functools

list1=[2,3,5,76,8]

def func(a,b):
    return a+b

res=functools.reduce(func,list1)

print(res)