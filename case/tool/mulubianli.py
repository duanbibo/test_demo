import os
import collections

def mulu(path):
      list=[]
      sum=0
      for i in os.walk(path):
            print(i)
            list.append(i)
            sum+=1
      lastlist=list.pop(1)
      print(sum)
      print(lastlist)
def digui_getAllDirAndFile(path, p=''):
    # 得到当前目录下所有的文件
    fileList = os.listdir(path)
    # print(fileList)
    p += "    "
    # 处理每一个文件
    for fileName in fileList:
        # isdir   isfile
        # 获取文件或文件夹的绝对路径
        fileAbs = os.path.join(path, fileName)
        # print(fileAbs)
        # 判断当前路径是不是文件夹
        if os.path.isdir(fileAbs):
            print(p + '文件夹' + fileName)
            # 递归调用
            digui_getAllDirAndFile(fileAbs, p)
        else:
            print(p + '普通文件' + fileName)
def shendu_getAllDirAndFile(path):
    stack = []  # 空元素
    stack.append(path)  # [r'C:\Users\xlg\Desktop\a']
    # 循环遍历处理栈的内容，当栈里面的内容为空时退出
    while len(stack) != 0:
        # 从栈里取出元素
        dirPath = stack.pop()
        # 遍历dirPath目录下的所有文件
        fileList = os.listdir(dirPath)
        for fileName in fileList:
            fileAbs = os.path.join(dirPath, fileName)
            if os.path.isdir(fileAbs):
                # 当当前目录时文件夹，进行入栈操作
                print('文件夹' + fileName)
                stack.append(fileAbs)
            else:
                print('普通文件' + fileName)
def guangdu_getAllDirAndFile(path):
    # 创建队列
    queue = collections.deque()
    # 添加元素
    queue.append(path)  #[a]
    while len(queue) != 0:
        # 移除队列中的元素
        dirPath = queue.popleft()
        # 获取dirPath下的所有文件及文件夹
        fileList = os.listdir(dirPath)
        for fileName in fileList:
            # 绝对路径
            fileAbs = os.path.join(dirPath, fileName)
            # 如果是文件夹就放到队列中
            if os.path.isdir(fileAbs):
                print('文件夹' + fileName)
                queue.append(fileAbs)
            else:
                print('文件' + fileName)







if __name__ == '__main__':
     # mulu(r"C:\Users\87842\Desktop\Work\uiTest-master")
     #digui_getAllDirAndFile(r"C:\Users\87842\Desktop\Work\uiTest-master")
      shendu_getAllDirAndFile(r"C:\Users\87842\Desktop\Work\uiTest-master")
     # guangdu_getAllDirAndFile(r"C:\Users\87842\Desktop\Work\uiTest-master")


