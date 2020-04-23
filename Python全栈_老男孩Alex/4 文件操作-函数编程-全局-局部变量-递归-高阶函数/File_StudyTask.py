# Author:Winnie Hu
f=open("backend",'r',encoding="utf-8")
#print(f.read())
#print(f.readline())

#打印行
# count=0
# for lines in  f:
#     count+=1
#     if count>4:
#         print(lines.strip())
#     else:
#         continue

#文件指定内容搜索并打印
# for lines in f:
#     if "www.oldboy.org" in lines:
#         print(lines)
#         print(f.readline())


#文件写入一段话
# b = '''{
#               'bakend': 'www.oldboy.org',
#               'record':{
#                   'server': '100.1.7.9',
#                   'weight': 20,
#                   'maxconn': 30
#               }
#           }'''
# with open("backend2", 'w', encoding="utf-8") as f:
#     f.write(b)


# 删除
with open("backend2",'r',encoding="utf-8") as f:
with open("backend2", 'w', encoding="utf-8") as f_new:
    for lines in f:
        if b in lines:
            lines=lines.replace(b,"")
     f_new.write(lines)