"""
错误和异常

"""
# 异常处理
from src.utils.custom import IllegalAgeException

while True:
    try:
        x = int(input("请输入年龄: "))
        if x < 0 or x >= 200:
            raise IllegalAgeException(x)  # 抛出异常
    except ValueError:  # 发生异常时执行
        print("您输入的不是数字，请再次尝试输入！")
    except IllegalAgeException as iae:
        print(iae)
    else:  # 未发生异常时执行
        print("你的年龄是", x, "岁")
    finally:  # 无论是否有异常都执行
        print('您输入的内容是', x)
