#  自定义异常类  继承Exception类
class IllegalAgeException(Exception):
    def __init__(self, value):
        self.value = "年龄不合法:" + str(value)

    def __str__(self):
        return repr(self.value)


"""
语法格式如下：

class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>
"""


class Animal:
    def desc(self):
        print("desc in Animal")

    def eat(self):
        return


"""
单继承
class DerivedClassName(BaseClassName1):
    <statement-1>
    .
    .
    .
    <statement-N>
    
多继承
class DerivedClassName(BaseClassName1，BaseClassName2...):
    <statement-1>
    .
    .
    .
    <statement-N>
"""


class Dog(Animal):
    # 类有一个名为 __init__() 的特殊方法（构造方法）,实例化时会自动调用
    def __init__(self, name="默认"):
        self.name = name
        return

    def desc(self):
        Animal.desc(self)  # 两种写法调用父类方法
        super(Dog, self).desc()  # super() 函数是用于调用父类(超类)的一个方法。
        print("desc in Dog", ", My name is ", self.name)

    def eat(self):
        print("Dog eat born")


class People:
    name = ''
    age = 0
    __weight = 0

    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def __str__(self):
        return "姓名：{0:10} 年龄：{1} 体重：{2}".format(self.name, self.age, self.__weight)


class Student(People):
    grade = ""

    def __init__(self, n, a, w, g):
        People.__init__(self, n, a, w)
        self.grade = g

    def __str__(self):
        return '{0} 年级：{1}'.format(People.__str__(self), self.grade)
