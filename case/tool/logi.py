import logging


logger=logging.getLogger("logTest") #定义日志收集器
logger.setLevel('DEBUG') #设置当前日志收集器的等级
fmt=logging.Formatter('%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s') #设置日志格式

file_handler=logging.FileHandler('./mylog.txt',encoding='utf-8')  #设置日志处理器输出到文件
file_handler.setLevel("DEBUG")  #设置日志处理器的级别
file_handler.setFormatter(fmt)   #设置输出格式

ch=logging.StreamHandler() #输出到控制台
ch.setLevel("DEBUG")
ch.setFormatter(fmt)

#将设置好的收集器和处理器，添加到日志系统中
logger.addHandler(file_handler)
logger.addHandler(ch)
print(__file__)

#将设置好的收集器和处理器，添加到日志系统中
logger.addHandler(file_handler)
logger.addHandler(ch)


if __name__ == '__main__':
      logger.debug("调试")


