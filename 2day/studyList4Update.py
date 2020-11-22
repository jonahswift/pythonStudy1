print('---------修改指定下标数据--------')
name_list = ['Tom', 'Lily', 'Rose']
name_list[1]='sss'
print(name_list)


print('--------逆置：reverse()---------')
num_list = [1, 5, 2, 3, 6, 8]
num_list.reverse()
print(num_list)

print('-------排序：sort()----------')
num_list = [1, 5, 2, 3, 6, 8]
num_list.sort()
print(num_list)



num_list.sort(reverse=True)
print(num_list)

print('--------复制函数：copy()---------')
name_list = ['Tom', 'Lily', 'Rose']
name_list2 =name_list.copy()
print(name_list2)

num_list3=name_list
print(num_list3)


