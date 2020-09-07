import os


def list_dir(cat):

    for path,dir_list,file_list in cat:

        # 遍历所有文件
        for file_name in file_list:
            files=os.path.join(path, file_name)

        #遍历所有子目录
        for dir_name in dir_list:
            dir_names=os.path.join(path, dir_name)

            size_count(dir_names)
            
    return files,dir_names


def size_count(dir_names):

    statinfo = os.stat(dir_names)
    # print(statinfo)
    if  statinfo.st_size>= 1024000:
        list_dir(dir_names)  #大于某个值就遍历该目录


if __name__ == '__main__':
    cat= os.walk(r"C:\Program Files\AISHU AnyShare")
    files, dir_names=list_dir(cat)



