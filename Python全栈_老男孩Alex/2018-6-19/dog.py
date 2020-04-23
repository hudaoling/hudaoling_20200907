# Author:Winnie Hu

class Dog:
    def __init__(self,name):
        self.name=name
#init传参数使用
    def bulk(self):
        print("%s:wang wang wang!" % self.name)

d1=Dog("jinmao")
d2=Dog("muyangquan")
d3=Dog("huanggou")
d1.bulk()
d2.bulk()
d3.bulk()


#类变量和实例变量的用途区别
#类变量是大家公用的属性，为了节省开销
class Person:
    cn="中国"
    def __init__(self,name,age,addr):
        self.name=name
        self.age=age
        self.addr=addr
p1=Person("alex","33","shanghai")
print(p1.cn)#按类变量cn="中国"


class Person:
    cn="中国"
    def __init__(self,name,age,addr,cn="china"):
        self.name=name
        self.cn=cn
        self.age=age
        self.addr=addr
p1=Person("alex","33","shanghai")
print(p1.cn)#按实例变量cn="china"


#私有属性(既变量)，只能在内部可以改，外部不可访问
class Person:
    cn="中国"
    def __init__(self,name,age,addr,cn="china"):
        self.name=name
        self.cn=cn
        self.__age=age
        self.__addr=addr#私有属性加“__”；外部无法用p1.__addr查看
    def age_add(self):
        self.__age+=1 #私有属性内部可以改(既方法和类里面可用)
        print("又长1岁了")
    def __age_mile(self):
        self.__age-=3 #私有方法内部可以改,外部不能访问
        print("又年轻3岁了")
    def show_status(self):#私有属性的查看方式，定义一个函数
        print("name:%s  age:%s addr:%s cn:%s"%(self.name,self.__age,self.__addr,self.cn))

p1=Person("alex",33,"shanghai")
p1.age_add()
print("私有属性",p1.show_status())
#print(p1.__addr)#私有属性，外部无法访问，所以报错'Person' object has no attribute '__addr'