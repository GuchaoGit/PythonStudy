# 斐波纳契数列
a, b = 0, 1
while b < 1000:
    print(b, end=' ')
    a, b = b, a + b
print()
print("--------------if 条件控制---------------")
c = 1
while c < 7:
    if c % 2 == 0:
        print(c, ' is even')
    else:
        print(c, ' is odd')
    c += 1
print('--------------狗年龄计算---------------')
age = int(input("请输入你家狗狗的年龄: "))
print("")
if age <= 0:
    print("你是在逗我吧!")
elif age == 1:
    print("相当于 14 岁的人。")
elif age == 2:
    print("相当于 22 岁的人。")
elif age > 2:
    human = 22 + (age - 2) * 5
    print("对应人类年龄: ", human)

# 退出提示
input("点击 enter 键继续")

print("--------------for 循环语句---------------")
'''
for <variable> in <sequence>:
    <statements>
else:
    <statements>
'''
count = 0
while count < 5:
    print(count, " 小于 5")
    count += 1
else:
    print(count, " 大于或等于 5")

languages = ['Python', 'Java', 'C']
for x in languages:
    print(x, end=" ")
    if x == 'C':
        break  # 跳出循环体  不再执行else
else:
    print('就列举了这么多')
print()
for x in range(5, 9):  # range()函数实现数字遍历  左闭右开
    print('range()函数生成', x)
