# Author:Winnie Hu
#for循环：i 是临时变量，在0-10以内循环的一组数
'''
for i in range(10):
    print("loop",i)
'''


#for循环：i 是临时变量，2是步长，相隔一个打印
"""
for i in range(0,10,2):
      print("loop",i)


for letter in 'Python':     # 第一个实例
   print('当前字母 :', letter)

fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # 第二个实例
   print('当前字母 :', fruit)
"""

#for循环与字典的结合使用
"""
city = {
'shanghai':9800,
'beijing':11000,
'shenzhen':8000,
'guagnzhou':6000,
}
print(city)
#print(city.keys())
#print(city.values())
#for i in city:print(i,city[i])

#for c in city.keys():print('City :', c)#求出各城市列表
for c in city.keys():print('AvgSalary:', city[c]) #求出各城市平均工资
for s in city.values(): print('AvgSalary2:', s)#求出各城市平均工资
"""

