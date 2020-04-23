d = {
'tenglan wu':'stu1101',
'longze luolan':'stu1102',
'yanfei luolan':'stu1103',
'mengfei luo':'stu1104',
}
info=[]
count=0
while count<3:
    name = input('请输入您的用户名：')
    count += 1
    if name in d and name not in info:
        count2 = 3
        while count2:
            password = input('请输入您的密码：')
            count2 -= 1
            if d[name]==password:
                print('welcome {} login...'.format(name))
                break#退出输入密码
            else:
                print('密码错误，你还有%s次机会，请重试'%count2)
                continue
        break#退出输入用户
    else:print('您输入的用户名不存在，请重新输入')
    info.append(name)
    #continue
else:print('您输入次数太多，请5分钟之后再试')#while条件不满足

print(info)