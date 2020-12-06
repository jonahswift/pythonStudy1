
def sum_number1(a,b):
    return abs(a)+abs(b) #绝对值

def sum_number(a,b):
    return round(a)+round(b) #四舍五入



def sum_number(a,b,f):
    return f(a)+f(b)

result= sum_number(3,-5,abs)
result1= sum_number(3.8,2.1,round)
print(result)
print(result1)