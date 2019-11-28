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
print("2/4=", 2/4, " 除法，浮点数")
print("2//4=", 2//4, " 除法，取整")
print("2%4=", 2 % 4, " 取余")
print("2**4=", 2**4, " 2的4次方")

print('-------------List(列表)-----------------')
# 表中元素的类型可以不相同
list1 = ['Hello', 110, 3.1416, 'PI']
list2 = ['Hi', 119, '着火了']
print(list1)
list3 = list1+list2
print(list3)  # 连接列表
list3[1:5] = []  # 将对应的元素值设置为 []
print(list3)
list3 = list3[-1::-1]  # 翻转字符串
print(list3)

print('-------------Tuple(元组)-----------------')
# 元组（tuple）与列表类似，不同之处在于元组的元素不能修改
tuple1 = ('Hello', 110, 3.1416, 'PI')
tuple2 = ('Hi', 119, '着火了')

