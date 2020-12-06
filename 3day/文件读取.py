f=open('test.txt')
read=f.readlines()
print(read )
f.close()


f=open('test.txt','w+')
f.write('write fdsd dfdf')
f.close()

f=open('test.txt')
read=f.readlines()
print(read)

f.close()