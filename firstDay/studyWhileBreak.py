#break
i=1
while i <= 5:
    if i==4:
        print('吃够了')
        break
    i +=1

#continue
i=1
while i<=5:
    if i==3:
        print('跳过3')
        i +=1
        continue
    print(i)
    i+=1