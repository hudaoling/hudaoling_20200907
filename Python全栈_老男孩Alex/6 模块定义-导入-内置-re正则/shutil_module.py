# Author:Winnie Hu

import shutil
#shutil是高级的 文件、文件夹、压缩包 处理模块

#shutil.copyfileobj(fsrc, fdst[, length])
#将文件内容拷贝到另一个文件中，可以部分内容
# f1=open("本节笔记",encoding="utf-8")
# f2=open("笔记2","w",encoding="utf-8")
# shutil.copyfileobj(f1,f2)

#直接拷贝文件到另一个文件
#shutil.copyfile("笔记2","笔记3")

#仅拷贝权限。内容，组，用户均不变,文件的状态信息可能变化了
#shutil.copymode("本节笔记","笔记3")

#拷贝状态的信息，包括mode bits,atime,mtime,flags
#shutil.copystat("本节笔记","笔记3")

#拷贝文件和权限（file and mode）
#shutil.copy("本节笔记","笔记3")

#拷贝文件和同时拷贝文件信息
#shutil.copy2("本节笔记","笔记3")

#递归的去拷贝文件
#shutil.copytree("package_test","new_package_test")
#递归的删除文件
#shutil.rmtree("new_package_test")

#文件的移动
#shutil.move()

#文件的打包
#不指定压缩存放路径时，就存在改py程序的同目录下
shutil.make_archive("shutil_archive_test","zip","Z:\TEMP\Crashpad")