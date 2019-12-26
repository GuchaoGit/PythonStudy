"""
标准库
"""

import glob
import os
import random
from src.utils.utils import is_leap_year

print('----------------操作系统接口--------------------')
path = os.getcwd()  # 获取当前目录
print("当前目录：{path}".format(path=path))
os.chdir("../..")  # 目录切换
path = os.getcwd()
print("当前目录：{path}".format(path=path))
os.chdir("PythonStudy/src")
print('----------------文件通配符--------------------')
fileList = glob.glob("*.py")
print(fileList)

print("随机数 {0}".format(random.randint(0, 9)))
print("{0} {1}".format(2018, "是闰年" if (is_leap_year(2018)) else "是平年"))
