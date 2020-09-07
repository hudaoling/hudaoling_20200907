# Author:Winnie Hu
class Animal(object):
     def __init__(self, name):
         self.name = name
     def talk(self):
        pass
         #raise NotImplementedError("Subclass must implement abstract method")

     @staticmethod#装饰器，
     def animail_talk(obj):
         obj.talk()

class Cat(Animal):
     def talk(self):
         print("%s: 喵喵喵!" % self.name)

class Dog(Animal):
     def talk(self):
         print("%s: 汪！汪！汪！"% self.name)

#一种接口，多种实现（将c.talk;d.talk合并定义为animail_talk函数）
def animail_talk(obj):
    obj.talk()#使用函数调用类里的talk()

d=Dog("jinmao")
d.talk()
c=Cat("yellowcat")
c.talk()

#统一的接口方法，函数实现
animail_talk(d)#等于d.talk()
animail_talk(c)#等于c.talk()

#统一的接口方法，装饰器实现，等同于上方的animail_talk
Animal.animail_talk(d)# @staticmethod#装饰器,在父类增加方法animail_talk(obj)
Animal.animail_talk(c)# @staticmethod#装饰器，在父类增加方法animail_talk(obj)