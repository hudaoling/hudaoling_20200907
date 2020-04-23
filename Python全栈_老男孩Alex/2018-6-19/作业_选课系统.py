# Author:Winnie Hu
"""本节作业: 选课系统
角色:学校、学员、课程、讲师
要求:
1. 创建北京、上海 2 所学校
2. 创建linux , python , go 3个课程 ， linux\py 在北京开， go 在上海开
3. 课程包含，周期，价格，通过学校创建课程
4. 通过学校创建班级， 班级关联课程、讲师
5. 创建学员时，选择学校，关联班级
5. 创建讲师角色时要关联学校，
6. 提供两个角色接口
6.1 学员视图， 可以注册， 交学费， 选择班级，
6.2 讲师视图， 讲师可管理自己的班级， 上课时选择班级， 查看班级学员列表 ， 修改所管理的学员的成绩
6.3 管理视图，创建讲师， 创建班级，创建课程
7. 上面的操作产生的数据都通过pickle序列化保存到文件里

学校
选择学校
1、创建班级
2、创建讲师
3、创建课程

讲师
1、查看班级
2、查看班级学员列表

学生
1、注册，选择学校
2、选择班级
3、报名缴费
"""
class Scholl(object):
    def __init__(self,sch_name,addr):
        self.sch_name = sch_name
        self.addr = addr
        self.courses=[] #用于存放课程
        self.grades = []  # 用于存放班级
        self.teachers = []  # 用于接收教师
        self.students = []  # 用于接收报名学生
    def Create_Course(self,course_type,cycle,price):#创建课程
        self.courses.append(Course(course_type,cycle,price))
        print("%s create one course '%s'"%(self.sch_name,course_type))

    def Create_Grade(self,grade_name,grade_num,bycourse,byteacher):
        self.grades.append(Grade(grade_name,grade_num,bycourse,byteacher))
        print("%s create one grade '%s'; course:%s is teached by %s "
              % (self.sch_name,grade_name,bycourse.course_type,byteacher.tea_name))
    def Hire_Teacher(self,tea_name,age,salary):
        self.teachers.append(Teacher(tea_name,age,salary))
        print("%s hire one teacher '%s'" % (self.sch_name,tea_name))
       # print("% is teaching %s"%(tea_name,course))
    def Enroll_Student(self,c_grade,stu_id,name,age,c_course):
        self.students.append(Student(c_grade,stu_id,name,age,c_course))
        pass


class Grade(object):
    def __init__(self,grade_name,grade_num,bycourse,byteacher):
        self.grade_name = grade_name
        self.grade_num = grade_num
        self.bycourse=bycourse
        self.byteacher=byteacher
    def tell(self):
        print('''---info of Grade:%s---
       grade_name:%s   grade_num:%s  bycourse:%s  byteacher:%s \n'''
        % (self.grade_name,self.grade_name, self.grade_num, self.bycourse.course_type, self.byteacher.tea_name))

class Course(object):
    def __init__(self,course_type,cycle,price):
        self.course_type = course_type
        self.cycle=cycle
        self.price=price
    def tell(self):
        print('''---info of course:%s---
    cycle:%s   price:%s\n''' % (self.course_type, self.cycle, self.price))

class Teacher(object):#教师类
    def __init__(self,tea_name,age,salary):
        self.tea_name = tea_name
        self.age = age
        self.salary=salary
        pass

class Student(object):#学生类
    def __init__(self,c_grade,stu_id,name,age,c_course):
        self.c_grade=c_grade
        self.name = name
        self.stu_id=stu_id
        self.age = age
        self.c_course=c_course
    def  pay_tuition(self,amount):#交学费
        print("%s had paid tution for %s "%(self.name,amount))
    def tell(self):
        print('''---info of student:%s---
            c_grade:%s   stu_id:%s  name:%s  age:%s course:%s \n'''
              % (self.name, self.c_grade.grade_name, self.stu_id, self.name, self.age,self.c_course.course_type))

print("实例化两个学校")
sch_sh=Scholl("SH_Uni","shanghai lianhangroad")#上海
sch_bj=Scholl("BJ_Uni","bei wangfujing")#北京
print(sch_sh.sch_name,"和",sch_bj.sch_name)
print(sch_sh.addr,"和",sch_bj.addr,"\n")

#print("实例化课程")
# cos_lin=Course("linux","3年",9800)
# cos_py=Course("python","2年",8800)
# cos_go=Course("go","1年",7800)
# print(cos_lin.course_type,cos_py.course_type,cos_go.course_type)
# print(sch_sh.course,"和",sch_bj.course,"\n")
# cos_lin.tell()

print("学校创建课程")
cos_go=sch_sh.Create_Course("go","3年",7800)
cos_lin=sch_bj.Create_Course("linux","3年",9800)
cos_py=sch_bj.Create_Course("python","2年",8800)
print("课程",sch_sh.courses,"和",sch_bj.courses)
print(sch_bj.courses[1].course_type,"\n")#查看某课程名称

print("学校创建讲师")
t1=sch_sh.Hire_Teacher("李大山",35,10000)
t2=sch_bj.Hire_Teacher("王语嫣",40,12000)
print("教师",sch_sh.teachers,sch_bj.teachers,"\n")

print("学校创建班级(关联了课程和教师)")
go01=sch_sh.Create_Grade("sh_初级_go",201801,sch_sh.courses[0],sch_sh.teachers[0])
py02=sch_bj.Create_Grade("bj_中级_python",201802,sch_bj.courses[0],sch_bj.teachers[0])
lin03=sch_bj.Create_Grade("bj_高级_linux",201803,sch_bj.courses[1],sch_bj.teachers[0])
print("班级",sch_sh.grades,sch_bj.grades)
print(sch_bj.grades[1].grade_name,"\n")#查看班级名称


#查看课程详细信息
sch_sh.courses[0].tell()
sch_bj.courses[0].tell()
sch_bj.courses[1].tell()

#查看班级详细信息
sch_sh.grades[0].tell()
sch_bj.grades[0].tell()
sch_bj.grades[1].tell()

#查看教师信息
print(sch_sh.teachers[0])
print(sch_sh.teachers[0].salary)

#创建学生以及学生报名
sch_bj.Enroll_Student(sch_bj.grades[1],6011,"Lisa",18,sch_bj.grades[1].bycourse)
sch_bj.Enroll_Student(sch_bj.grades[0],6012,"winnie",16,sch_bj.grades[0].bycourse)
sch_sh.Enroll_Student(sch_sh.grades[0],6013,"ryan",19,sch_sh.grades[0].bycourse)
sch_bj.students[0].tell()
sch_bj.students[1].tell()
sch_sh.students[0].tell()

#学生交学费
sch_bj.students[0].pay_tuition(9800)
sch_bj.students[1].pay_tuition(8800)
sch_sh.students[0].pay_tuition(7800)


#查看学生\教师\课程\班级列表
for stu in  sch_bj.students:
    print(stu.c_grade.grade_name,stu.stu_id,stu.name,stu.age,stu.c_course.course_type)

for tea in sch_bj.teachers:
    print(tea.tea_name,tea.age,tea.salary)

for course in sch_bj.courses:
    print(course.course_type,course.cycle,course.price)

for grade in sch_bj.grades:
    print(grade.grade_name,grade.grade_num,grade.bycourse.course_type,grade.byteacher.tea_name)