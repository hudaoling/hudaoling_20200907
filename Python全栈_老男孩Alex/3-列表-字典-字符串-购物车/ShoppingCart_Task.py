# Author:Winnie Hu

Salary=int(input("Salary:")) #输入工资
goods_list=[[1,"mac",6880],[2,"iphone",5880],[3,"jbl",988],[4,"bike",598],[5,"lenovo",3299]]
print(goods_list) #输出商品列表
#print(goods_list[1])
count = 0
while True:
  choose_goods=goods_list[int(input("please choose goods："))] #用户选择商品
  print(choose_goods) #输出用户选择的商品
  choosegoods_price=int(choose_goods[2])
#print(type(int(choose_goods[2])))
  if Salary < choosegoods_price:
     print("Sorry,Your balance is not enough,please choose again")
  else:
    have_choose=[choose_goods]
    Salary = Salary - choosegoods_price

print(have_choose)