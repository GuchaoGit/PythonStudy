"""
数据结构
"""
from src.utils.utils import print_array, get_now_time

print(get_now_time())

list1 = [1, 2, 3]
print_array('原始数组', list1)
list1.append(4)
print_array('末尾插入4', list1)
list2 = [5, 6, 7]
list1.extend(list2)
print_array('扩充列表', list1)
list1.insert(0, -1)
print_array('开头插入-1', list1)
list1.pop(len(list1) - 1)  # 移除指定位置的元素
print_array('移除最后一位7', list1)
list1.remove(3)  # 删除第一个为0的元素，没有则报错
print_array('移除元素值为3的元素', list1)
try:
    print('获取index(3)=', list1.index(3))  # 返回第一个值为3的索引
except ValueError:
    print('list1中没有 3 元素')
list1.reverse()
print_array('翻转', list1)
list1.sort()
print_array('排序', list1)
list3 = list1.copy()  # 返回列表的浅复制，等于a[:]
list4 = list1[:]
print("原id=", id(list1), "新id=", id(list3), "浅复制id=", id(list4))
list5 = [3 * x for x in list1 if x > 0]  # 列表推导式+if 过滤器
print_array('列表推导生成：', list5)
del list5[1:3]  # 删除一个元素或一个切割
print_array('删除[1:3]', list5)
