# Author:Winnie Hu
#key values 字典
#value 的数据类型，使用就像上学用的字典，通过笔划、字母来查对应页的详细内容。
#字典是无序的
info={
'stu1101':"tenglan wu",
'stu1102':"longze luolan",
'stu1103':"longze luolan",
'stu1104':"mengfei luo",
}
b={
'stu1101':"yanfei wang",
1:3,
2:5,
}

#查找
#print(info)
#print(info["stu1101"]) #取出对应的值
#print(info.get("stu1106"))#获取到stu1103对应的值，不存在就返回none
#print("stu1106" in info)#输出True or False
#print(info.get("stu1105"))#不存在就返回none

#修改和增加
#info["stu1101"]="武藤兰"  #变更、修改对应的值
#info["stu1101"]="cangjingkong" #没有的话，就是新增某值
#print(new_info)

#----del删除----
#del info 删除字典
#del info["stu1101"] #删除指定的值
#info.pop("stu1101")#删除指定的值，标准用法
#info.popitem()#随机删除
#print(info)

#---输出key或values等操作
#print(info.values())
#print(info.keys())
#info.update(b)#把两个字典info和b合并，交叉的key就更新key对应的值
#print(info.items())#字典转成列表
#new_info=info.fromkeys([6,7,8],"test") #创建了一个新的字典，每个key值默认都为test，其实与info没关系，可以用dict
#new_info=dict.fromkeys([6,7,8],"test")#初始化一个新的字典
#print(new_info)

#踩坑的经验
#三个key 6\7\8对应的值都是[1,{"name":"alex"},777]，共享一个内存地址
#所以，改了一个，其他的也会一起变化
#new_info=dict.fromkeys([6,7,8],[1,{"name":"alex"},777])
#new_info[7][1]['name']="jack chen"

#字典循环
for i in info:
  print(i,info[i]) #打印key,values

for k,v in info.items(): #把字典转成列表，但是当数据量大时，转换时间很长，不建议使用
    print(k,v) #打印key，


"""#多级字典嵌套及操作
#三级嵌套的例子(第三级是list)
av_catalog = {
    "欧美":{
        "www.youporn.com": ["很多免费的,世界最大的","质量一般"],
        "www.pornhub.com": ["很多免费的,也很大","质量比yourporn高点"],
        "letmedothistoyou.com": ["多是自拍,高质量图片很多","资源不多,更新慢"],
        "x-art.com":["质量很高,真的很高","全部收费,屌比请绕过"]
    },
    "日韩":{
        "tokyo-hot":["质量怎样不清楚,个人已经不喜欢日韩范了","听说是收费的"]
    },
    "大陆":{
        "1024":["全部免费,真好,好人一生平安","服务器在国外,慢"]
    }
}

av_catalog["大陆"]["1024"][1] += ",可以用爬虫爬下来"
print(av_catalog["大陆"]["1024"])

av_catalog.setdefault("台湾",{"baidu":[1,2]}) #先取第一层，存在就取值，不存在就新增
print(av_catalog)
"""