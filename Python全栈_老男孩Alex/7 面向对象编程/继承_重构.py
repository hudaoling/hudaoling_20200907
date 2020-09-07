# Author:Winnie Hu

# Author:Winnie Hu

#class People:经典类写法
class People(object):#新式类写法
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eat(self):
        print("%s is eating..."%self.name)
    def sleep(self):
        print("%s is sleeping..."%self.name)
    def talk(self):
        print("%s is talking..."%self.name)

class Man(People):#Man是People的子类，继承了父类的属性和方法
    def __init__(self,name,age,money):#子类重构方法
        #People.__init__(self,name,age)
        super(Man,self).__init__(name,age)#新式类写法，与上一行相同，可以不写父类名，用于多继承的方式
        self.money=money#重构增加属性money

    def piao(self):#子类可增加新方法
        self.money-=500
        print("%s is piaoing and money is "%self.name)
    def sleep(self):#子类也可重构父类方法(增加修改父类方法)
        People.sleep(self)#调用父类方法
        print("man is sleeping...")#新增父类方法

class Woman(People):#Woman是People的子类，继承了父类的属性和方法
    def get_birth(self):#子类法的新增方法
        print("%s is born a baby..."%self.name)
    def sleep(self):
        People.sleep(self)
        print("Woman is sleeping...")
m1=Man("Alex",33,10000)#实例化的对象m1
m1.eat()
m1.piao()
m1.sleep()
print(m1.name,m1.age,m1.money)

w1=Woman("ChenRonghua",26)#实例化的对象w1
w1.get_birth()
w1.sleep()
print(m1.name)

