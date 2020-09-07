# Author:Winnie Hu

# Author:Winnie Hu

#多继承

class People(object):#父类
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.friends=[]
    def eat(self):
        print("%s is eating..."%self.name)
    def sleep(self):
        print("%s is sleeping..."%self.name)
    def talk(self):
        print("%s is talking..."%self.name)

class Relation(object):#父类
    def make_friends(self,obj): #obj=w1,w2对象
        print("%s is making friends with %s"%(self.name,obj.name))#注意多个参数时，要用括号
        self.friends.append(obj)

#Relation为什么不需要定义参数？因为对象m1和w1已经具备父类People的属性。
#子类继承顺序是从左到右，对象向类传参顺序是从左到右

class Man(People,Relation):#Man多继承People和Relation两个类的方法

    def __init__(self,name,age,money):#子类重构方法
        super(Man,self).__init__(name,age)
        self.money=money

    def piao(self):#子类可增加新方法
        self.money-=500
        print("%s is piaoing and money is "%self.name)
    def sleep(self):#子类法的新增方法
       # People.sleep(self)
        print("man is sleeping...")

class Woman(People,Relation):#Woman多继承People和Relation两个类的方法
    def get_birth(self):#子类法的新增方法
        print("%s is born a baby..."%self.name)
    def sleep(self):
        People.sleep(self)
        print("Woman is sleeping...")

m1=Man("Alex",33,10000)#实例化的对象m1
print(m1.name,m1.age,m1.money)

w1=Woman("ChenRonghua",26)#实例化的对象w1
w2=Woman("guana",30)#实例化的对象w2


m1.make_friends(w1)#一个朋友
m1.make_friends(w2)#第二个朋友
w1.name="chenrong"#第一个朋友改名

print(m1.friends)#这个是对象内存地址


print(m1.friends[0].name) #朋友列表里面的名字也跟着变化了
print(m1.friends[1].name)