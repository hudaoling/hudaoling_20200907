# Author:Winnie Hu

#角色用户定义
#role1
name='Alex'
role='terrorist'
weapon='AK47'
life_value=100
#role2
name2='Jack'
role2='police'
weapon2='B22'
life_value2=100

#role3
name3='Rain'
role3='terrorist'
weapon3='C33'
life_value3=100
money3=10000

#role4
name4='Eric'
role4='police'
weapon4='B51'
life_value4=100
money4=10000

#roles,相当于上述的role1-rloe4,用列表展示
roles = {
    1:{'name':'Alex',
       'role':'terrorist',
       'weapon':'AK47',
       'life_value': 100,
       'money': 15000,
       },
    2:{'name':'Jack',
       'role':'police',
       'weapon':'B22',
       'life_value': 100,
        'money': 15000,
       },
    3:{'name':'Rain',
       'role':'terrorist',
       'weapon':'C33',
       'life_value': 100,
       'money': 15000,
       },
    4:{'name':'Eirc',
       'role':'police',
       'weapon':'B51',
       'life_value': 100,
       'money': 15000,
       },
}
print(roles[1]) #Alex
print(roles[2]) #Jack

def shot(by_who):
    #开了枪要减子弹数
    pass

def got_shot(who):
    #中枪后减血
    who['life_value']-=10
    pass

def buy_gun(who,gun_name):
    #检查钱够不够，买了枪后要扣钱
    pass


#代码改成OOP中的“类”来实现
class Role:#类的定义，Role是类的名称
    n=123 #类变量
    name='我是类变量'#类变量
    def __init__(self,name,role,weapon,bullet=10,life_value=100,money=15000):
        #init构造函数（定义参数），在实例化时，用于接收传来的参数值
        self.name=name#r1.name=name 实例变量，赋给了具体的实例
        self.role=role#r1.role=role实例变量，作用域就是实例本身
        self.weapon=weapon#实例变量或（静态属性）
        self.bullet=bullet
        self.life_value=life_value
        self.money=money
    def __del__(self):
        print("%s 彻底死了..."% self.name)
        #析构函数,在对象释放销毁的时候自动执行，相当于删除了r1,r2两个实例化的对象
        # 在程序中间也可用 del  r1,r2  删除实例化的对象 r1,r2

# 定义类的方法（可调用函数），完成一系列的游戏动作
    def shot(self):#类的方法，功能（或动态属性）
        self.bullet-=1
        print("shooting...")

    def got_shot(self):
       self.life_value -= 10
       print("%s ah...,I got shot..."% self.name)

    def buy_gun(self,gun_name):
         self.money-=1000
         print("%s just bought %s" %(self.name,gun_name))

#把一个类变成了一个具体对象的过程叫实例化
#r1,r2是类的调用，实例化过程（初始化一个类）,拥有了自己的属性
#r1,r2就是Role类的两个实例（两个对象）
r1_old=Role('Alex','police','AK47')#生成一个角色
del r1_old #析构函数del，删除实例化的对象

r1=Role('Alex','police','AK47')#生成一个角色
r2=Role('Jack','terrorist','B22')#生成另一个角色

print(Role)#Role是一个类，存于内存中，输出结果是一个class
print(shot,got_shot,buy_gun)#这3个是函数（既 类的方法），存于内存中,输出结果是内存地址function
print("r1,r2是类的对象",r1,r2)#__main__.Role object at 0x035785B0
#r1，r2将自己传参给self，同时写入内存地址
#r1，r2的属性（'Alex','police','AK47'等）传递给Role（name,role,weapon）,也写入内存地址

print("n是类变量:",Role.n)#n存在于Role类的内存里
print("先实例找后在类里找：",r1.n,r1.name) #先找实例本身，没有的话再去类里面找

print("游戏前:",r1.name,r1.bullet,r1.life_value,r1.money)
r1.buy_gun("BK47")#角色Alex买了一把BK47，花了1000
#相当于r1.buy_gun=Role.buy_gun(r1)
r1.shot()#角色Alex射击了一枪
r1.got_shot()#角色Alex中枪了，减血10
print("游戏后:",r1.name,r1.bullet,r1.life_value,r1.money)

#可以对角色进行修改
r1.name='alex'
r1.role='Polic'
r1.money=20000
print("修改后:",r1.name,r1.role,r1.weapon,r1.money)

#可以对角色增加、删除属性（属性既变量）
r1.bullet_proof=True#增加防弹衣
print("增加后:",r1.name,r1.role,r1.money,r1.bullet_proof)
del  r1.weapon #删除武器
#print("删除后:",r1.weapon) #报错：Role' object has no attribute 'weapon'

#在实例里面改变类变量（不影响类变量，只在实例里增加了一个“与类变量同名”的实例变量）
r1.n='实例改变类变量'#相当于在实例r1里面增加了一个实例变量n
print("r1:",r1.name,r1.n)#输出n“实例改变类变量”
print("r2:",r2.name,r2.n)#输出n"123"
print(Role.n)#输出n"123"

#类变量自变更的影响范围（因为r1本身有n变量，类变量的变化对它无影响）
Role.n='abc'  #类变量n由123变成abc
print("r1:",r1.name,r1.n)#r1有自己的n,不受类变量影响，输出n“实例改变类变量”
print("r2:",r2.name,r2.n)#r2没有n,就跟着类变量变化，输出n 由123变成"abc"
