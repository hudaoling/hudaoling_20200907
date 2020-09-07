# Author:Winnie Hu

#动态方法
class Dog(object):
    def __init__(self,name):
        self.name=name

    def eat(self,food):
        print("动态方法self.：","%s is eating %s"%(self.name,food))
d=Dog("jinmao")
d.eat("baozi")

#静态方法
class Dog(object):
    def __init__(self,name):
        self.name=name
    # 静态方法,实际上跟类没什么关系了，就可理解为类下面的一个普通函数
    @staticmethod#只装饰某一方法，不影响下面其它方法
    def eat(name,food):
        print("静态方法@staticmethod：","%s is eating %s"%(name,food))

    def talk(self):
      print("不受影响", "%s is talking" % (self.name))
d=Dog("jinmao")
d.eat("jinmao","baozi")
d.talk()

#类方法,作用在类变量
class Dog(object):
    name="huabao"#类变量
    def __init__(self,name):
        self.name=name
    #类方法，只能访问类变量，不能访问实例变量。无法访问实例里面的变量。
    #一般用于强制该方法只能调用类变量。
    @classmethod
    def eat(self,food):
        print("类方法@classmethod：","%s is eating %s"%(self.name,food))
d=Dog("jinmao")
d.eat("baozi")


#属性方法
class Dog(object):
    def __init__(self,name):
        self.name=name
        self.__food=None
#属性方法，把一个方法变成一个静态属性。
    @property
    def eat(self):
        print("属性方法@property：","%s is eating %s"%(self.name,self.__food))

#如果要给eat赋值时，可以采用以下方法
    @eat.setter
    def eat(self,food):
        print("set to food:",food)
        self.__food=food#给私有属性self.__food赋值food

d=Dog("jinmao")
d.eat #d.eat变成了一个属性（既变量）。属性方法不用括号，不用传参，只能用常量值（例如"baozi"）
d.eat="niurou" #赋值后，d.eat也会跟着变为“niurou”
d.eat

#del d.name  #属性既变量，可以删除
#print(d.name)

del d.eat #属性方法默认无法删除

    @eat.deleter
    def eat(self):
        del self.__food
        print("删完了")

