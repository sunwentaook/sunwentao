
class Money(object):
    def __init__(self):
        self.__money = 0
    @property
    def getMoney(self):
        return self.__money
    @money.setter
    def setMoney(self,value):
        if isinstance(value,int): # isinstance 判断
            self.__money = value
        else:
            print('error:不是整数型')
m = Money()
m.setMoney(100.5)
print(m.getMoney())
#m.money = 100.5
#print(m.money)
