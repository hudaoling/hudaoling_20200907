

user_info={'dachengzi':{'pwd':'123123'},
           'kangbazi':{'pwd':'kkkkkk'}}
dic = user_info.get('dachengzi')
print(dic)

def login(request):
    if request.method=="get":
        return render(request,'login.html')
    if request.method=="POST":
        u=request.POST.get("username")
        p=request.POST.get("pwd")
        dic=user_info.get(u)
        if not dic:
            return render(request, 'login.html')#如果用户不在列表中，重定向登录页

        if dic['pwd']==p:
            res=redirect('/index/')  #如果用户密码正确，重定向首页
            res.set_cookies('username1111',u) #同时：设置浏览器cookie
            return res
        else:
            return  render(request, 'login.html') #如果密码错误，返回登录页



def index(request):
    v=request.COOKIES.get('username1111')
    if not v:
        return  redirect('/login/')  #用户下次登录时，先检查cookie,如果有cookie,则直接返回首页，否则重定向到登录页
    return render(request,'index.html',{'current_name':v})