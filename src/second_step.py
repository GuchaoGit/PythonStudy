# 迭代器
# 基本方法：iter() 和 next()

list1 = [1, 2, 3, 4, 5]
it = iter(list1)  # 创建迭代器对象
for x in it:
    print(x, end=" ")

while True:
    try:
        print(next(it))
    except StopIteration:
        print('遍历完成')
        break


#  创建一个迭代器
#  1、实现两个方法 __iter__() 与 __next__()
class MyNumbers:
    def __iter__(self):
        self.a = 1
        print('__iter__', self.a)
        return self

    def __next__(self):
        if self.a <= 3:
            y = self.a
            self.a += 1
            return y
        else:  # 2、通过 StopIteration 异常标识迭代的完成
            raise StopIteration


myClass = MyNumbers()
myiter = iter(myClass)
try:
    print(next(myiter))
    print(next(myiter))
    print(next(myiter))
    print(next(myiter))
except StopIteration:
    print('遍历结束')


#  生成器  使用了 yield 的函数被称为生成器（generator）
def fibonacci(n):  # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if counter > n:
            return
        yield a
        a, b = b, a + b
        counter += 1


f = fibonacci(5)
while True:
    try:
        print(next(f), end=' ')
    except StopIteration:
        print('遍历完成')
        break
