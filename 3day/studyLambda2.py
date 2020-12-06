fn1= lambda a,b : a if a>b else b
print(fn1(5,3))

students=[{'name':'tom','age':33},
          {'name':'dom2','age':34},
          {'name':'com3','age':35}]

students.sort(key=lambda x:x['name']) #升序
print(students)

students.sort(key=lambda x:x['name'],reverse=True)#降序
print(students)

students.sort(key=lambda y:y['age'])
print(students)