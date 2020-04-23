# Author:Winnie Hu

#广度优先查找法（python3默认按广度优先来继承）
class A:
    def __init__(self):
        print("A")
class B(A):
    pass
    # def __init__(self):
    #     print("B")
class C(A):
    pass
    # def __init__(self):
    #     print("C")
class D(B,C):
    pass
    # def __init__(self):
    #     print("D")

#广度优先查找法：D没有去找B（B找到了就结束），B没有找C（C找到了就结束），C再没有就找A
#广度优先：先横向查，再纵向查
obj=D() #先在B找，在C找，再到A里去找


#深度优先查找法（python2 经典类是按深度优先来继承，新式类是按广度优先来继承的）
class A:
    def __init__(self):
        print("A")
class B(A):
    pass
    # def __init__(self):
    #     print("B")
class C(A):
    pass
    # def __init__(self):
    #     print("C")
class D(B,C):
    pass
    # def __init__(self):
    #    print("D")

#深度优先查找法：D没有去找B（B找到了就结束），B没有找A（A找到了就结束），A再没有就找C
#深度优先：先纵向查，再横向查
obj2=D() #先在B找，在A找，再到C里去找