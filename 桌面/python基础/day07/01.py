class Person(object):
    def __init__(self,name,age,taste):
        self.name = name
        self._age = age
        self.__taste = taste
    def showperson(self):
        print(self.name)
        print(self._age)
        print(self.__taste)
    def _work(self):
        print('工作')
    def __away(self):
        print('away')
class Student(Person):
    def constrcution(self,name,age,taste):
        self.name = name
        self._age = age 
        self.__taste = taste
    def showstudent(self):
        print(self.name)
        print(self._age)
        print(self.__taste)
    @staticmethod
    def testbug():
        pass
class _Bug(object):
    @staticmethod
    def showbug():
        print('showbug')
s1 = Student('王',18,'剑')
s1.showperson()
# 无法访问 __taste() 导致报错
s1.showstudent()
s1.constrcution('子',15,'gongzhu')
s1.showperson()
