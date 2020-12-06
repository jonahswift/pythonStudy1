#conding:utf-8
f=open('test.txt','a+')
f.seek(0)
read=f.readlines()
print(read)
f.seek(2)
f.write('''write fdsd dfdf1
        二
    对方是否都是
dfggdf''')
f.seek(0)
read=f.readlines()
print(read )

f.close()


with open('test.txt','r') as f:
    data = f.readlines()
    print(data)

