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
