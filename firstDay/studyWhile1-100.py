#计算1加到100的和

n=1
sum=0

while n<=100:
    sum = sum+n
    n=n+1

print('sum:为',sum)

#计算1加到100中偶数的和
a=2
sum1=0
while a<=100:
   sum1 = sum1+a
   a +=2
print(sum1)


print('------------------')
b=1
sum2=0
while b<=100:
    if b%2 ==0:
        sum2 = sum2 + b
    b+=1

print('sum2',sum2)


print('------------------')
