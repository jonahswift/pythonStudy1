#三元表达式
a=1
b=2

if a>b:
    c=a
else:
    c=b
print(c)


c=a if a>b else b
print(c)