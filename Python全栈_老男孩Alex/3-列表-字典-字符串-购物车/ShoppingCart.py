# Author:Winnie Hu
'''---------Day 2---------
程序：购物车程序
需求:
    启动程序后，让用户输入工资，然后打印商品列表
    允许用户根据商品编号购买商品
    用户选择商品后，检测余额是否够，够就直接扣款，不够就提醒
    可随时退出，退出时，打印已购买商品和余额
程序：购物车优化
用户入口：
1.商品信息存在文件里
2.已购商品，余额记录。长时间留存
商家入口：
2.可以添加商品，修改商品价格
'''
shopping_list=[]
product_list=[('Iphone',5800),
              ('bike',800),
              ('Mac',3000),
              ('IWatch',10600),
              ('Coffee',31),
              ('Python',120)]
salary=input("Salary:") #输入工资
if salary.isdigit():
    salary=int(salary)
    while True:
        for index,item in enumerate(product_list):#enumerate,index 增加编号索引
            #for item in product_list:
            #print(product_list.index(item),item)#功能同上，增加商品编号
             print(index,item)
        user_choose=input("请选择您需要的商品>>>：")
        if user_choose.isdigit():
            user_choose=int(user_choose)
            if user_choose < len(product_list) and user_choose >= 0: #用户选择在范围内
                p_item=product_list[user_choose]#用户所选商品
                if p_item[1]<=salary: #买得起,商品价格低于工资
                    shopping_list.append(p_item)#购物车列表
                    salary-=p_item[1]#增加购物车后，工资余额减少
                    print("Added %s into shopping cart,your current balance is \033[31;1m%s\033[0m"%(p_item,salary))
                else:
                    print("\033[41;1m您的余额还剩[%s]啦，还买个毛线\33[0m"%salary)
            else:print("product code is not exist...")
#增加字体颜色\033[31;1m%s\033[0m",31是红色，32是绿色;41是背景红，42是背景色绿

        elif user_choose=='q':
            print("----shopping list----")
            for p in shopping_list:
                print(p)
            print("Your current balance:",salary)
            exit()#位置要摆好，容易出错
        else:print("invalid product option,please try again")
else:print("invalid input,please input your salary again")
#print(shopping_list)