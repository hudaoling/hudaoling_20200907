import os

cat = os.walk(r"C:\Program Files\AISHU AnyShare")

for path, dir_list, file_list in cat:
    # print(dir_list)

    catnumbers = len(file_list)

    # 遍历所有文件
    for file_name in file_list:
        files = os.path.join(path, file_name)

    # 遍历所有子目录
    for dir_name in dir_list:
        dir_names = os.path.join(path, dir_name)
        print(dir_names)
        statinfo = os.stat(dir_names)
        print(statinfo)
        if statinfo.st_size >= 1024:
        #     # 大于某个值就再次遍历该目录
            for ps, dl, fl in os.walk(dir_names):
                    fienumbers=len(fl) #len是计算文件数量，f1是list格式
                    print(fienumbers)
                    print(catnumbers)



