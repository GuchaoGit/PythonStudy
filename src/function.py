"""
定义函数语法：
def 函数名（参数列表）:
    函数体

以下是调用函数时可使用的正式参数类型：
1、必需参数
2、关键字参数
3、默认参数
4、不定长参数
"""


def hello(name):
    print('Hello ', name)


def area(width, height):
    return width * height


def change_int(a):  # 必需参数
    """
    在 fun（a）内部修改 a 的值，只是修改另一个复制的对象，不会影响 a 本身。
    :param a: 只是传递的值，
    :return:新对象
    """
    a = 6
    return a


def change_list(la):  # 必需参数
    """
    在 fun（la）内部修改 la 的值，会影响 la 本身。
    :param la:传递可变对象
    """
    la += [4, 5, 6]
    print('函数内取值', la)


hello('guc')
w, h = 4, 5
print('width = ', w, ' height = ', h, ' area = ', area(w, h))
# 在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象
intA = 4
print(change_int(intA))
print(intA)

listA = [1, 2, 3]
change_list(listA)
print('函数外取值：', listA)

hello(name="谷超")  # 关键字参数


def print_person(name, age=0):  # 默认参数
    print("姓名：", name, " 年龄：", age)


print_person("guc")  # 年龄默认0  默认参数不是必需
print_person("guc", 29)
print_person(age=30, name="谷超")


def print_all(tag, *vartuple):  # 不定长参数
    """
    加了星号 * 的参数会以元组(tuple)的形式导入
    :param tag:
    :param vartuple: 以元组(tuple)的形式导入
    :return:
    """
    print('输出：', tag, end=' ')
    print(vartuple)
    print(len(vartuple))


print_all('dog like eat', 'meat', 'bone')


def print_all_another(tag, **var_args_dict):
    """
    加了两个星号 ** 的参数会以字典的形式导入
    :param tag:
    :param var_args_dict:
    :return:
    """
    print('输出：', tag, end=' ')
    print(var_args_dict)
    print(var_args_dict.keys())


print_all_another('你的性别：', a='男', b='女')

"""
lambda 函数的语法

lambda [arg1 [,arg2,.....argn]]:expression
"""
sum = lambda arg1, arg2: arg1 + arg2
print("1 + 3 = ", sum(1, 3))

'''
# 3.8新增 / 用来指明必须使用位置参数，不能使用关键字参数的形式
def f(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)
'''

