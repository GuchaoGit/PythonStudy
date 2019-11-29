# 标准数据类型
"""
Number(数字)
String(字符串)
List(列表)
Tuple(元组)
Set(集合)
Dictionary(字典)
"""
# 四种数据类型：int(整数) bool（布尔） float（浮点数） complex（负数）
a, b, c, d = 20, 5.5, True, 4 + 3j  # 同时给多个变量赋值
print(type(a), type(b), type(c), type(d))  # type()函数获取变量类型
isInt = isinstance(a, int)  # isinstance() 判断对象类型
print(isInt)
print(isInt + 1)  # True和False的值还是1和0，可与数字相加

print('-------------数值运算-----------------')
print("2/4=", 2 / 4, " 除法，浮点数")
print("2//4=", 2 // 4, " 除法，取整")
print("2%4=", 2 % 4, " 取余")
print("2**4=", 2 ** 4, " 2的4次方")

print('-------------List(列表)-----------------')
# 表中元素的类型可以不相同
list1 = ['Hello', 110, 3.1416, 'PI']
list2 = ['Hi', 119, '着火了']
print(list1)
list3 = list1 + list2
print(list3)  # 连接列表
list3[1:5] = []  # 将对应的元素值设置为 []
print(list3)
list3 = list3[-1::-1]  # 翻转字符串
print(list3)

print('-------------Tuple(元组)-----------------')
# 元组（tuple）与列表类似，不同之处在于元组的元素不能修改
tuple1 = ('Hello', 110, 3.1416, 'PI')
tuple2 = ('Hi', 119, '着火了')
print(tuple1 + tuple2)

print('-------------Set(集合)-----------------')
# 基本功能是进行成员关系测试和删除重复元素。
# 创建一个空集合必须用 set() 而不是 { }
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
print(student)  # 输出集合，重复的元素被自动去掉
if 'Rose' in student:
    print("Rose 在集合中")
else:
    print('Rose 不在集合中')
set1 = set('abcdabc')
set2 = set('adf')
print(set1 - set2)  # 差集
print(set1 | set2)  # 并集
print(set1 & set2)  # 交集
print(set1 ^ set2)  # 不同时存在

print('-------------Dictionary(字典)-----------------')
# 创建空字典使用 { }
dict0 = {'name': '百度', 'code': 1, 'site': 'www.baidu.com'}
print(dict0.keys())
print(dict0.values())
print(dict0['name'])  # 输出键为 name 的值

dict1 = {x: x**2 for x in (2, 4, 6)}
print(dict1)
dict2 = dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])
print(dict2)
