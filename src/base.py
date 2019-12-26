import random  # 随机数
from math import ceil

print('-------------运算符------------')
a = -3
b = 2
print('-3//2=', a // b)
print('a==b', a == b)
print('a=', a)
a += 1
print('a +=1, a=', a)
a **= 2
print('a **= 2, a=', a)
print('-------------逻辑运算符（and or not）------------')
# and or not
if a and b:
    print("a=", a, ',b=', b, '都是true')
else:
    print('a和b至少有个不为true')
if not a:
    print('a为false')
else:
    print('a为true')
print('-------------成员运算符(in /not in)------------')
# in /not in
fruits = ['Apple', 'Banana', 'Orange', 'Pear', 'Grape']
for x in fruits:
    print(x)
print('-------------身份运算符(is /is not)------------')
# is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等
c = a
print('a=', a, ',c=', c)
if c is a:
    print('c和a有相同的标识')
else:
    print('c和a没有相同的标识')
if (id(a) == id(c)):
    print('c和a有相同的标识')
else:
    print('c和a没有相同的标识')
d = [1, 2, 3]
e = d[:]  # 值相等
f = d  # 相同的引用
print(f is d)
print(e is d)
print(e == d)

print('-------------Number------------')
# // 得到的并不一定是整数类型的数，它与分母分子的数据类型有关系
print(7.0 // 3)
print(7 // 3)
print(ceil(-3.1))  # 向上取整
print('随机数')
print('随机：', random.random())
print('随机：', random.choice(range(1, 10)))

print('-------------字符串格式化------------')
world = 'World'
print(f'Hello{world}')  # f-string 是 python3.6 之后版本添加的
print('Hello %s %d' % (world, 2))

print('-------------列表------------')
# + 号用于组合列表，* 号用于重复列表
print('原始：', ['Hi`'])
print('原始*4：', ['Hi`'] * 4)
list1 = [1, 4, 9]
list2 = [x ** 2 for x in [1, 2, 3]]  # 列表推导式
print(len(list1), max(list1))
print(list2)

print('-------------元组------------')
tuple0 = ()  # 空元组
tuple1 = (5,)  # 元组中只包含一个元素时，需要在元素后面添加逗号，否则括号会被当作运算符
tuple2 = (5)
print(type(tuple1))
print(type(tuple2))

print('-------------字典------------')
dict0 = {}  # 空字典
dict1 = {'a': 456, 'b': 789}
dict0['name'] = 'guc'
print(dict0)
print(dict1)

print('-------------集合------------')
set1 = {'abcdddd'}  # 创建集合
set2 = set()  # 空集合
print(set1)
set3 = set('abcdeddde')  # 将字符串转为集合
print(set3)
set4 = {x for x in 'abcdef' if x not in 'abc'}  # 集合推导式
print(set4)
set4.add('guc')
print(set4)
set4.discard('4')  # 移除集合中的元素，且如果元素不存在，不会发生错误
print(set4)
set5 = set(('Google','Taobao', 'Baidu', 'Google'))   # 将元组转为set5
print(set5)
