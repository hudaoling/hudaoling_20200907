# Author:Winnie Hu

class Scholl(object):
    members=0
    def __init__(self,name,addr):
        self.name=name
        self.addr=addr
        self.students=[]#初始化空列表，用于接收报名学生
        self.staffs=[]#初始化空列表，用于接收教师
    def  enroll(self,stu_obj):#stu_obj某学生对象
        print("为学员%s办理注册手续"%stu_obj.name)
        self.students.append(stu_obj)
    def  hire(self,staff_obj):#staff_obj雇佣的教师
        print("雇佣新员工%s"%staff_obj.name)
        self.staffs.append(staff_obj)

class SchollMember(object):#父类，公有属性name,age,sex
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def tell(self):
       # print("---info of %s"%st)
         pass

class Teacher(SchollMember):#Teacher子类，重构自己的方法
    def __init__(self, name, age, sex, salary,course):
        super(Teacher,self).__init__(name,age,sex)
        self.salary = salary#增加属性
        self.course = course#增加属性
    def tell(self):#增加方法：打印教师信息
        print('''---info of Teacher:%s---
              Name:%s
              Age:%s
              Sex: %s
              Salary: %s
              Course: %s'''%(self.name,self.name,self.age,self.sex,self.salary,self.course))

    def teach(self):#老师在上课
        print("%s is teaching coure [%s]"%(self.name,self.course))

class Student(SchollMember):#Student子类，重构自己的方法
    def __init__(self, name, age, sex, stu_id, grade):
        super(Student,self).__init__(name, age, sex)
        self.stu_id = stu_id#增加属性
        self.grade = grade#增加属性

    def tell(self):#增加方法：打印学生信息
        print('''---info of Teacher:%s---
                     Name:%s
                     Age:%s
                     Sex: %s
                     stu_id: %s
                     grade: %s''' % (self.name, self.name, self.age, self.sex, self.stu_id, self.grade))
    def pay_tuition(self,amount):
        print("%s had paid tution for $%s"%(self.name,amount))

sch1=Scholl("上海中学","闵行区") #实例化一个学校：上海中学
t1=Teacher("Alex",33,"男",10000,"英语")
t2=Teacher("Jack",38,"男",15000,"数学")
s1=Student("Annie",12,"男","s112","二年级")
s2=Student("Alas",12,"女","s112","三年级")

t1.tell()#打印教师alex的详细信息
s1.tell()#打印学员Annie的详细信息

sch1.hire(t1)#上海中学雇佣了t1:Alex
sch1.hire(t2)
print(sch1.staffs) #雇佣的教师存到Scholl的教师列表
print(sch1.staffs[0].salary)#可以查看教师alexde 工资，==t.salary

sch1.enroll(s1)#上海中学录取了s1:Annie
sch1.enroll(s2)
print(sch1.students[0].name) #可以查看学员的姓名等，==s1.name

print(sch1.members)
t1.teach() # sch1.staffs[0]=t1
sch1.staffs[0].teach()#相当于t1.teach()


s1.pay_tuition(3000)
s2.pay_tuition(3000)#相当于下面的for循环
for stu in  sch1.students:
    stu.pay_tuition(3000)

