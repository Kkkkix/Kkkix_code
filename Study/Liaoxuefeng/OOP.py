class Student(object):
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        if isinstance(gender, str):
            if gender.lower() == "male":
                self.__gender = "male"
            elif gender.lower() == "female":
                self.__gender = "female"
            else:
                print("The input format is incorret, please input female/male.")


# # 测试:
# bart = Student('Bart', 'male')
# if bart.get_gender() != 'male':
#     print('测试失败!')
# else:
#     bart.set_gender('female')
#     if bart.get_gender() != 'female':
#         print('测试失败!')
#     else:
#         print('测试成功!')


class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count = Student.count + 1


# # 测试:
# if Student.count != 0:
#     print('测试失败!')
#
# else:
#     bart = Student('Bart')
#
#     if Student.count != 1:
#         print('测试失败!')
#     else:
#         lisa = Student('Lisa')
#         Bob = Student('Bob')
#         if Student.count != 3:
#             print('测试失败!')
#         else:
#             print('Students:', Student.count)
#             print('测试通过!')


# 练习 使用@property
# 请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：

class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self,value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height

# # 测试:
# s = Screen()
# s.width = 1024
# s.height = 768
# print('resolution =', s.resolution)
# if s.resolution == 786432:
#     print('测试通过!')
# else:
#     print('测试失败!')


class Chain(object,):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain(f'{self._path}/{path}')

    def __str__(self):
        return self._path

    def __call__(self, *args, **kwargs):
        return Chain(f'{self._path}/{str(*args)}')

    __repr__ = __str__


# print(Chain().user('michael').repos)
# print(Chain().use.repos)


from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

# # 测试
# for name, member in Month.__members__.items():
#     print(name, '=>', member, ',', member.value)

