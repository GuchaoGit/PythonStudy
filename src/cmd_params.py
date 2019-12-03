import sys
import src.utils.utils as utils

print('命令行参数')
if sys.argv.__len__() <= 1:
    print('没有多余的参数了')
else:
    for i in sys.argv:
        print(i)
print(utils.get_now_time())
print(dir(utils))
