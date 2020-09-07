

'''zip在英文中有拉链的意思，我们由此可以形象的理解它的作用：将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同。
语法：
zip([iterable, ...])
示例：'''

a = [1,2,3]
b = [4,5,6]
c = [4,5,6,7,8]


#zip(iter1,iter1)
zipp_a = zip(a,b)     # 打包为元组的列表
print([i for i in zipp_a],'\n')
print(list(zip(a,b)),'\n') #这一步相当于上面两步
'''[(1, 4), (2, 5), (3, 6)] '''

zip_b=zip(a,c)
print([i for i in zip_b],'\n') # 元素个数与最短的列表一致,多余部分省略
print('list(zip(a,c):',list(zip(a,c)),'\n')
'''[(1, 4), (2, 5), (3, 6)] '''

print('*zip(a,b):',*zip(a,b),'\n')




# zip(*zip(iter1,iter1))
x,y=zip(*zip(a,b))
print('zip(*zip(a,b)):',x,y,'\n') # 与 zip 相反，可理解为解压，为zip的逆过程，可用于矩阵的转置
'''(1, 2, 3) (4, 5, 6) '''
print(list(zip(*zip(a,b))))
'''[(1, 2, 3), (4, 5, 6)]'''

class MyClass(object):

    def method(self,arg):
        print(arg)

my_object = MyClass()
my_object.method("foo")