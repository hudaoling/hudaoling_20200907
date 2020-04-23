# Author:Winnie Hu
#正则表达式：复杂的查询条件
import re
#match方法是从字符的开头开始，只取符合条件的第一个;
#search方法是从字符串中搜索，只取符合条件的第一个;
#findall取回符合条件的所有值,就不需要group()方法
#split分割字符串
#sub替换


# '^'  匹配字符开头，若指定flags MULTILINE,
# 这种也可以匹配上(r"^a","\nabc\neee",flags=re.MULTILINE)
res=re.match("^Chen","ChenRonghua123")
print(res)#匹配结果
print("^：",res.group())#查看匹配到内容

#'\d' 匹配数字0-9  '\d+' 代表取一个或多个数字
res=re.match("^Chen\d+","Chen321Ronghua123")
#print(res)
print("\d+：",res.group())

#'.' 默认匹配除\n之外的任意一个字符，若指定flag DOTALL,则匹配任意字符，包括换行
res=re.match(".+","Chen321Ronghua123")#从开头匹配字符
print("C.+：",res.group())#   .匹配一个字符，.+匹配所有字符


#'$' 匹配字符结尾，判断是不是以某个字符结尾的
# 或e.search("foo$","bfoo\nsdfsf",flags=re.MULTILINE).group()也可以
res=re.search("R.+a$","Chen321Ronghua123a")#从R开始a结束取值字符，非数字(a$一定是最后一个字母是a，而不是截取到a)
print("R.+：",res.group())

#[a-zA-Z]匹配从R开头到a结束的字符，不包含数字
res=re.search("R[a-z]+a","Chen321RongHua123aRonghua")#从R开始取值
res2=re.search("R[a-zA-Z]+a","Chen321RongAHua123aRonghua")#从R开始取值
print(res)
print("R[a-z]a：",res.group())
print(res2)
print("R[a-zA-Z]a：",res2.group())

# '*' 匹配*号前的字符0次或多次，re.findall("ab*","cabb3abcbbac")  结果为['abb', 'ab', 'a']

t1=re.search("#.+#","1123#hello#")
print("#.+#：",t1.group())

# '+' 匹配前一个字符1次或多次，re.findall("ab+","ab+cd+abb+bba") 结果['ab', 'abb']

# '?' 匹配问号前一个字符1次或0次
t2=re.search("aal?","alxaaaba")#aal在字符串从左至右匹配查找
print("a?:",t2)
t2=re.search("a?","lxaaaba")
print("a?:",t2)

# '{m}'匹配前一个字符m次,需要匹配上几次
res=re.search("[0-9]{3}","aa1x2a345aab")
print("[0-9]{3}：",res.group())

# '{n,m}'匹配前一个字符n到m次，re.findall("ab{1,3}","abb abc abbcbbb") 结果'abb', 'ab', 'abb']
res=re.search("[0-9]{2,3}","aa1x23a345aab")
res2=re.findall("[0-9]{2,3}","aa1x23a345aab")#findall找出所有匹配条件的值
print("search[0-9]{2,3}：",res.group())
print("findall[0-9]{2,3}：",res2)#不需要用group()

# '|'匹配|左或|右的字符，re.search("abc|ABC","ABCBabcCD").group() 结果'ABC'
print(re.search("abc|ABC","ABCBabcCD").group())
print(re.findall("abc|ABC","ABCBabcCD"))

# '(...)'括号是分组匹配，re.search("(abc){2}a(123|456)c", "abcabca456c").group() 结果 abcabca456c
print(re.findall("(abc){2}.+(xyz){2}","abcabca456cxyzxyz"))

#'\A' 只从字符开头匹配，re.search("\Aabc","alexabc") 是匹配不到的
#判断是不是以什么开头，相当于^
print(re.search("\Aalex","alexabc").group())
print(re.search("\A[0-9]{3}","567alexabc").group())

#'\Z' 匹配字符结尾，同$
#如下例子：数字开头，小写字母结尾
print(re.search("\A[0-9].+[a-z]\Z","999A%yyyz").group())

#'\d' 匹配数字0-9
#'\D' 匹配非数字
print(re.search("\D+","123A%$ +……\ntest").group())

#'\w' 匹配[A-Za-z0-9]
print(re.search("\w+","123A%$ +eop\ntest").group())

#'\W' 匹配非[A-Za-z0-9]
print(re.search("\W+","123A%$ +eop\ntest").group())

#'\s' 匹配空白字符、\t、\n、\r , re.search("\s+","ab\tc1\n3").group() 结果 '\t'
print(re.search("\s+","123A%$+eop \n    ").group())


#(?P<name>...)' 分组匹配
res=re.search("(?P<id>[0-9]+)(?P<name>[a-zA-Z]+)","abcd1234alex@34").group()
#groupdict成字典格式
res=re.search("(?P<id>[0-9]+)(?P<name>[a-zA-Z]+)","abcd1234alex@34").groupdict()
print(res)
print(res['id'])

#身份证号码示例：cardid=
cardid=re.search("(?P<province>[0-9]{4})(?P<city>[0-9]{2})(?P<birthday>[0-9]{8})","360602201809090019").groupdict("city")
print("身份信息",cardid)

#split分割字符串
print(re.split("[0-9]+","abc12de3f45GH"))#以数字来分割

#sub替换
print(re.sub("[0-9]+","|","abc12de3f45GH"))
print(re.sub("[0-9]+","|","abc12de3f45GH",count=2))

#\反斜杠的匹配使用
print(re.search(r"\\","abc12de\\3f45GH").group())

#忽略大小写
print(re.search("[a-z]+","atABCup12de45GH",flags=re.I).group())

#去除多行模式的搜索；\n在开头第一个是，也可以被排除
print(re.search("^d","\nde45\nGH",flags=re.M).group())

#匹配任意模式；\n也包含在内
print(re.search(r".+","re.S\nabc\nedk",flags=re.S).group())
