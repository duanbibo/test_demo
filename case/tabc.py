import  os

# def  bianlimulu(path):
#          mulu=os.listdir(path)
#          p=" "
#          for mu in mulu:
#                absmulu=os.path.join(path,mu)
#                if os.path.isdir(absmulu):
#                      print(p+"文件夹"+mu)
#                      bianlimulu(absmulu)
#                else:
#                      print("普通文件"+mu+p)

def  bianlishendu(path):
    list = []  # 空元素
    list.append(path)            # [r'C:\Users\xlg\Desktop\a']
    # 循环遍历处理栈的内容，当栈里面的内容为空时退出
    while len(list) != 0:
        # 从栈里取出元素
        dirPath = list.pop()
        # 遍历dirPath目录下的所有文件
        print("dirPath是" + str(dirPath))
        fileList = os.listdir(dirPath)
        print("fileList是"+str(fileList))

        #结果为目录下的所有文件件
        for fileName in fileList:
            fileAbs = os.path.join(dirPath, fileName)
            if os.path.isdir(fileAbs):
                # 当当前目录时文件夹，进行入栈操作
                print('文件夹' + fileName)
                list.append(fileAbs)
            else:
                print('普通文件' + fileName)



bianlishendu(r"G:\Charles")
#bianlimulu(r"G:\Charles")