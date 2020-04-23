# Author:Winnie Hu


# __doc__,输出：类的描述信息
class Foo:
    """ 描述类信息，这是用于看片的神奇 """
    def func(self):
        pass
print(Foo.__doc__)


#__module__ 表示当前操作的对象在那个模块
#__class__    表示当前操作的对象的类是什么
# from lib.aa import C
# obj=C()#实例化C
# print(obj.__module__)#输出lib.aa,即：输出模块
# print(obj.__class__)#输出lib.aa.C，即：输出类


#__call__ 实例化对象后加括号，触发执行。
# 注：构造方法的执行是由创建对象触发的，即：对象 = 类名() ；
# 而对于 __call__ 方法的执行是由对象再加括号触发的，即：对象() 或者 类()()
class Foo:
    def __init__(self):
        pass
    def __call__(self, *args, **kwargs):
        print('running call',args,kwargs)

obj = Foo()  # 执行 __init__
#obj()  # 不用__call__时报错,TypeError: 'Foo' object is not callable


obj = Foo()
obj(1,"a","test",name="alex")
Foo()("man",sex="男")


#__dict__ 查看类或对象中的所有成员
class Province:
    country = 'China'
    def __init__(self, name, count):
        self.name = name
        self.count = count
    def func(self, *args, **kwargs):
        print('func')

# 获取类的成员，即：静态属性和动态方法，以一个字段的方式呈现
#不包括实例属性
print(Province.__dict__)

#获取实例化对象的成员，即实例属性，以一个字段的方式呈现
#不包括类属性
obj1 = Province('HeBei', 10000)
obj2 = Province('HeNan', 3888)
print("对象obj1的成员",obj1.__dict__)
print("对象obj2成员",obj2.__dict__)# 获取 对象obj1 的成员

#__str__ 如果一个类中定义了__str__方法，那么在打印 对象 时，默认输出该方法的返回值。
class Dog(object):
    def __init__(self,name):
        self.name=name
        self.__food=None
    def __str__(self):
        return  "obj:%s"%self.name
obj=Dog("jinmao")
print(obj)#如果不用__str__ return，输出<__main__.Dog object at 0x0105BCD0>，内存地址
print(obj)#用了str后，输出 obj:jinmao，用户自定义的print内容

#__getitem__、__setitem__、__delitem__
#用于索引操作，如字典。以上分别表示获取、设置、删除数据
class Foo(object):
    def __init__(self):
        self.data={}#self.data是一个字典

    def __setitem__(self, key, value):#实例化对象可以增加字典
        self.data[key]=value #赋值，相当于obj.data[name]="alex"
        print('__setitem__', key, value)

    def __getitem__(self, key):#实例化对象可以get字典的key
        print('__getitem__', key)
        return self.data.get(key)

    def __delitem__(self, key):#可以删除key
        print('__delitem__', key)

obj = Foo()
obj['name']="alex" #自动触发执行 __setitem__
print(obj.data)
print(obj['name'])  #自动触发执行,__getitem__

del obj['name']#触发了一个执行动作，并未真正删除字典。
del obj['abcdefg']#删除了一个不存在的，也不会报错


#__new__\__metaclass
"""obj 是通过 Foo 类实例化的对象，其实，不仅 obj 是一个对象，
Foo类本身也是一个对象，因为在Python中一切事物都是对象。
如果按照一切事物都是对象的理论：obj对象是通过执行Foo类的构造方法创建，
那么Foo类对象应该也是通过执行某个类的 构造方法 创建。
"""
class Foo(object):
    def __init__(self,name):
        self.name=name
f=Foo("alex")

#对象f是Foo类的一个实例，Foo类对象是 type 类的一个实例
print(type(f))   #<class '__main__.Foo'>,f对象来自于类<Foo>
print(type(Foo)) #<class 'type'>,Foo对象来自于类<type>

def func(self):
    print("hello %s"%self.name)
def __init__(self,name,age):
    self.name=name
    self.age=age

Foo=type('Foo',(object,),{'talk':func,'__init__':__init__})#type类，进行实例化成Foo，type是类的类
print("Foo是type的实例对象",type(Foo))

f=Foo("ryan",33) # Foo类，进行实例化成f,Foo既是对象又是类。
f.talk()

#类的创建原理




