#求三个数之和

a=int(input("输入数字："))
b=int(input("输入数字："))
c=int(input("输入数字："))

def sum (a,b,c):
    sum=a+b+c
    return sum

def ave (a,b,c):
    #除法结果默认为浮点型
    ave=sum(a,b,c)/3
    #int强制转换
    ave=int(ave)
    return ave


print(sum(a,b,c))
print(ave(a,b,c))
