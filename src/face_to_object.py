"""
面向对象

"""
from src.utils.custom import (Dog, People, Student)

dog = Dog()
dog.desc()
dog.eat()

people = People('基础人', 24, 80)
print(str(people))

student = Student('学生', 18, 60, '大一')
print(str(student))
