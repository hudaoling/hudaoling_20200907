

names=['alex','jack']
try:
    names[3]
except IndexError as e:
    print("1列表操作错误", e,'\n')#列表取值错误

data={}
try:
    data['name']
except KeyError as e: #KeyError关键字错误
    print("2没有这个key",e,'\n')


try:
    data['name']
    names[3]

except KeyError as e:
    print("3没有这个key",e,'\n')
except IndexError as e:
    print("4列表操作错误",e,'\n')


print('-----------------------')
try:
    # data['name']
    # names[3]
    names[1]
except (IndexError,KeyError) as e:
    print("5出错了",e,'\n')
except Exception as e: #不区分错误类型,抓取所有的错误类型，建议用在排错的最后面
    print(6,e,'\n')

else:#如果没有抓到错误，就返回正常值
    print('一切正常')

finally:#不管有没有错，都执行
    print("不管有没有错，都执行")

#缩进错误，语法错误，python是无法抓到的





# 自定义异常
class AlexException(Exception):
    def __init__(self,msg):
        self.message=msg

try:
    raise AlexException('数据库连不上异常')  #raise手动触发异常，文本内容就是报错内容
except AlexException as e:
    print(e)