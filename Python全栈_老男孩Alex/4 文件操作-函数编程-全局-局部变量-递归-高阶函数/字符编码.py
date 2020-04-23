# Author:Winnie Hu
"""http://www.cnblogs.com/yuanchenqi/articles/5956943.html
http://www.diveintopython3.net/strings.html
需知:
1.在python2默认编码是ASCII, python3里默认是unicode
2.unicode 分为 utf-32(占4个字节),utf-16(占两个字节)，utf-8(占1-4个字节)，
so utf-16就是现在最常用的unicode版本，不过在文件里存的还是utf-8，因为utf8省空间
3.在py3默认是unicode,在解码encode时,在转码的同时还会把string 变成bytes类型，
decode在解码的同时还会把bytes变回string"""

#-*-coding:gb2312 -*-
import  sys
print(sys.getdefaultencoding())
msg="我爱北京天安门" #这个文件是utf8
print("msg---》",msg)
#msg_gb2312=msg.decode("utf-8").encode("gb2312") 错误的方法
msg_gb2312=msg.encode("gb2312")#python默认是unicode,就直接encode解码即可
msg_gbk=msg.encode("gbk")#gbk和gb2312输出内容一致
gb2312_to_unicode=msg_gb2312.decode("gb2312")#gb2312转码为unicode
gb2312_to_utf8=msg_gb2312.decode("gb2312").encode("utf8")

print("msg_gb2312---》",msg_gb2312)
print("msg_gbk---》",msg_gbk)
print("gb2312_to_unicode---》",gb2312_to_unicode)
print("gb2312_to_utf8---》",gb2312_to_utf8)


utf8_gbk=gb2312_to_utf8.decode("utf-8").encode("gbk")
print("utf8_gbk---》",utf8_gbk)

utf8_unicode=gb2312_to_utf8.decode("utf-8")
print("utf8_unicode---》",utf8_unicode)

#decode转码，encode解码