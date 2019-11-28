print("Hello")
a = 1
if a < 2:
    print("A 小于 2")
elif a >= 2 & 2 <= 5:
    print("A 介于2和5之间")
# 相同的缩进代表代码块
else:
    print("A 大于5")

# 多行语句用反斜杠来实现
hello = "Hello" + \
        "World" + \
        ",Mr.Gu"
print(hello)

# python中数字有四种数据类型：int(整数) bool（布尔） float（浮点数） complex（负数）
# 字符串
# '''或""" 实现多行字符串
str1 = '''hello
my name is Guc'''
print(str1)

# 反斜杠会转义使用r可让其不转义
print('------------------------------')
str2 = "Hi\nMy name is Lily"
str3 = r"Hi\nMy name is Lily"
print(str2)
print(str3)

print('------------------------------')
# 截取：变量[头下标:尾下标:步长]
str4 = "HelloWorld"
print(str4[5:])  # 输出从第三个开始后的所有字符
print(str4 * 2)  # 输出两次

print('-------------实现不换行需要在变量末尾加上 end=""-----------------')
x = 'a'
y = 'b'
# 默认换行输出
print(x)
print(y)

print(x, end=" ")
print(y, end=" ")
print()
