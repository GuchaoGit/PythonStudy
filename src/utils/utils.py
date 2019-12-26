import datetime

print(__name__)
if __name__ == '__main__':
    print('程序自身在运行')
else:
    print('我来自另一模块')


def print_array(tag, array):
    print(tag, ":", array)


def get_now_time():
    return datetime.datetime.now()


# 是否是闰年
def is_leap_year(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True  # 整百年能被400整除的是闰年
            else:
                return False
        else:
            return True  # 非整百年能被4整除的为闰年
    else:
        return False
