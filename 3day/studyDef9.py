def return_num():
    return 10,20

num1,num2=return_num()
print(num1)
print(num2)


dict1={'name':'tom','age':33}

a,b=dict1

print(a)
print(b)
print(dict1[a])
print(dict1[b])

a=10
b=20
c=0
c=a
a=b
b=c
print(a)
print(b)


a,b=2,6
b,a=a,b
print(a)
print(b)