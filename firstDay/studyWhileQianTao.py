print(5*'*')

n=0
while n<5:
    print('*',end='')
    n+=1

print('--------------------------------------')
a=0
while a<5:
    b = 0
    while b<5:
        print('*',end='')
        b+=1
    print()
    a+=1




print('打印左下三角形--------------------------------------')
a=0
b=0
n=8#n控制行数
while a<n:
    b = b-a
    while b<a+1:
        print('* ',end='')
        b+=1
    print()
    a+=1

print('打印右下直角三角形--------------------------------------')
n=8#n控制行数
i=1
b=0
for i in range(1,n+1):
    for b in range(0,n-i):
        print('  ',end='')
    for b in range(0,i):
        print('* ',end='')
    print('')

print('打印左上三角形--------------------------------------')
i=1
b=0
n=8#n控制行数
for i in range(1,n+1):
    for b in range(0,n-i+1):
        print('* ',end='')
    print('')

print('打印右上三角形--------------------------------------')
i=1
b=0
n=8#n控制行数
for i in range(1,n+1):
    for b in range(0,i-1):
        print('  ',end='')
    for b in range(0,n-i+1):
        print('* ',end='')
    print('')

print('打印等边三角形--------------------------------------')
i=1
a=0
n=6
for i in range(i,n+1):
    for a in range(0,n-i):
        print('  ',end='')
    for a in range(0,2*i-1):
        print('* ',end='')

    print('')
print('打印等腰三角形--------------------------------------')
i=1
a=0
n=6
for i in range(i,n+1):
    for a in range(0,n-i):
        print(' ',end='')
    for a in range(0,2*i-1):
        print('*',end='')

    print('')

print('while打印等腰三角形--------------------------------------')
i=0
n=9#n控制行数
while i<=n:
    j = 0
    while  j<n-i:
        print(' ',end='')
        j+=1
    j = 0
    while j<i+1:
        print('* ',end='')
        j += 1
    print()
    i += 1
