print('------------------while-----------------')
name_list = ['Tom', 'Lily', 'Rose']
i=0
while i<len(name_list):
    print(name_list[i])
    i+=1

print('-------------------for----------------')
name_list = ['Tom', 'Lily', 'Rose']
for i in name_list:
    print(i)

print('------------------列表嵌套-----------------')
name_list = [['⼩明', '⼩红', '⼩绿'], ['Tom', 'Lily', 'Rose'], ['张三', '李四',
'王五']]

print(name_list[1])
print(name_list[1][2])
