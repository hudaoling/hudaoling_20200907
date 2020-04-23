# Author:Winnie Hu
#局部变量和全局变量
#CTRL+?，批量注释
#不应该在函数里面更改全局变量，千万不要操作
# 全局与局部变量
# 在子程序中定义的变量称为局部变量，在程序的一开始定义的变量称为全局变量。
# 全局变量作用域是整个程序，局部变量作用域是定义该变量的子程序。
# 当全局变量与局部变量同名时：
# 在定义局部变量的子程序内，局部变量起作用；在其它地方全局变量起作用。


school="oldboy edu." #全局变量，在函数内外均可使用
print("函数调用前", school)

def change_name(name):
    print("before change",name)
    name="Alex Li"#局部变量，只在此函数里生效，改变变量值name,
    age=23 #局部变量，这个函数就是这个变量age的作用域
    print("after change",name,age)
    #global school #禁止使用:声明全局变量,并做更改,因为函数调用关系多而复杂，影响其他程序
    school="Mage Linux"
    print("函数调用后,变量重新赋值",school)

name="alex"
change_name(name)#传参name="alex"给change_name函数
print(name)
print("全局变量",school)


#字符串和数字“不能”在函数的局部变量来改变（全局变量）
#列表、字典、集合、类都可在函数的（局部变量）来改变（全局变量）
school="oldboy edu."
names=["alex","jack","rain"]
def change_name():
    names[0]="ryan"#函数里面变更全局变量
    print("inside func",names)
change_name()
print(names)