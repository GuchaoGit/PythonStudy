"""
输入和输出
Python两种输出值的方式: 表达式语句和 print() 函数
第三种方式是使用文件对象的 write() 方法，标准输出文件可以用 sys.stdout 引用。
"""
# str()： 函数返回一个用户易读的表达形式。
# repr()： 产生一个解释器易读的表达形式。
import math
import src.utils.utils as utils

s = 'Hello, World'
number = 1 / 7
print(str(s))
print(str(number))  # 返回一个用户易读的表达形式
print(repr(s))
print(repr(number))
# 在括号中的数字用于指向传入对象在 format() 中的位置，如下所示：
print('{1} 和 {0}'.format('Google', 'Runoob'))
# 关键字参数
print('{name}网址： {site}'.format(name='百度', site='www.baidu.com'))
# !a (使用 ascii()), !s (使用 str()) 和 !r (使用 repr()) 可以用于在格式化某个值之前对其进行转化
print('常量PI的值近似为：{}'.format(math.pi))
print('常量PI的值近似为：{!r}'.format(math.pi))
# 可选项 : 和格式标识符可以跟着字段名
print('常量PI的值近似为：{:.3f}'.format(math.pi))
# 旧式格式化字符串
print('常量PI的值近似为：%5.3f' % math.pi)
print('---------------------------------')
str2 = input("请输入：")
print('你输入的内容是：', str2)
print('----------------打开一个文件-----------------')
f = open("E:/PythonStudy/test.txt", "w")
f.write("Python 是一个非常好的语言。\n是的，的确非常好!!\n")
f.write(str(utils.get_now_time()))
f.write('\n--------------------end---------------------------\n')
f.close()
print('----------------文件写入成功-----------------')
print('----------------读取文件：E:/PythonStudy/test.txt-----------------')
fr = open("E:/PythonStudy/test.txt", 'r')
str3 = fr.read()
print(str3)
fr.close()
print('----------------文件读取完毕-----------------')
