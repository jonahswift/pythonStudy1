list1=[1,2,3,4,5,6]

def funcc(a):
    return  a**2

res=map(funcc,list1)
res1=list(map(funcc,list1))

print(res)
print(list(res))
print(res1)