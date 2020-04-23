# Author:Winnie Hu

#username = input("username:")
#password = input("password:")
#print(username,password)
#raw_input 2.x=input 3.x

#用此办法可以让用户输入信息，并打印信息

"""字符串拼接法"""
name = input("name:")
age = input("age:")
job = input("job:")
salary = input("salary:")
info='''
----- info of ''' + name + ''' ----
Name: ''' + name + '''
Age: ''' + age + '''
Job: ''' + job + '''
Salary:''' + salary + '''
'''
print(info)


# % 占位符方法 （%s代表string,;%d代表整数；%f代表浮点数）
name = input("name:")
age = int(input("age:")) #int()强制转换为interger
print(type(age)) #打印变量类型
print(type(age),type(str(age))) #打印变量类型
job = input("job:")
print(type(job)) #打印变量类型
salary = input("salary:")
info='''
----- info of %s ----
Name:%s
Age:%d
Job:%s
Salary:%s
''' % (name,name,age,job,salary)
print(info)


#format官方建议方法，格式化拼接 ,{_name}是参数
name = input("name:")
age = int(input("age:")) #int()强制转换为interger
print(type(age)) #打印变量类型
print(type(age),type(str(age))) #打印变量类型
job = input("job:")
print(type(job)) #打印变量类型
salary = input("salary:")
info2='''
----- info of {_name} ----
Name:{_name} 
Age:{_age} 
Job:{_job} 
Salary:{_salary} 
''' .format(_name=name,_age=age,_job=job,_salary=salary)
print(info2)

info3='''
----- info of {0} ----
Name:{0} 
Age:{1} 
Job:{2} 
Salary:{3} 
''' .format(name,age,job,salary)
print(info3)


#用户输入input内容，记录到字典里面
name = input("name:")
age = int(input("age:")) #int()强制转换为interger
print(type(age),type(str(age))) #打印变量类型
job = input("job:")
print(type(job)) #打印变量类型
salary = input("salary:")
info={
name:age,
job:salary,
}
print(info)
print(info[name])