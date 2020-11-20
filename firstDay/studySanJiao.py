print('while打印菱形(n为单数)--------------------------------------')
n=9
i=1
while i<=n:
    if i<=n/2+1:
        #上半边空白三角形
        a=0
        while a<=n/2-i:
            print('  ',end='')
            a+=1
        #上半部三角形
        a=0
        while a<i*2-1:
            print('* ',end='')
            a+=1
    else:
        a=0
        while a<i-n/2-1:
            print('  ',end='')
            a +=1
        a=0
        while a<=(n-i)*2:
            print('* ',end='')
            a +=1
    i+=1
    print()





