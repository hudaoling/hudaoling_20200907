
def bulk(self):
    print("%s is yelling....",self.name)

class Dog(object):

    def __init__(self,name):
        self.name=name

    def eat(self,food):
        print("%s is eating...",food)



d=Dog('xiaohua')
choice=input(">>").strip()

# print(hasattr(d,choice))
#hasattr判断d对象下input输入的(name_str字符串形式)方法是否存在，返回true or false

# print(getattr(d,choice))
#getattr接受用户input输入的方法，返回的是类的方法，<bound method Dog.eat of <__main__.Dog object at 0x000001BA265A5320>>
#方法不存在报错:AttributeError: 'Dog' object has no attribute 'talk'


if hasattr(d,choice):
    func=getattr(d,choice)
    func("bone")
else:
    '''动态装配方法'''
    setattr(d,choice,bulk)#将用户input的任意方法都转换成指定方法bulk
    func=getattr(d,choice)
    func(d)

    '''动态装配属性'''
    setattr(d,choice,22)#将用户input的任意属性值都转换成指定值22
    print(getattr(d,choice))
    #如果用户输入的属性值已经存在，可以通过setattr重新赋值


'''delattr:删除bulk方法后，再打印bulk方法将报错'''
if hasattr(d,choice):
    delattr(d,choice)
    print(d.bulk)


