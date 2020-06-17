import re
import random

# 识别函数助手    \转义符 __redom(10)
FUNC_EXPR = '__.*?\(.*?\)'

def randomint(length):
    '''
    生成指定长度随机数字
    :param length:
    :return:
    '''
    s = [str(i) for i in range(10)]
    return ''.join(random.sample(s,length))




def build_param(self, string):
      '''
      识别${key}并替换成全局变量池的value,处理__func()函数助手
      :param str: 待替换的字符串
      :return:
      '''

      # 遍历所有取值并做替换
      keys = re.findall(self.EXPR, string)
      for key in keys:
            value = self.saves.get(key)
            string = string.replace('${' + key + '}', str(value))

      # 遍历所有函数助手并执行，结束后替换  __ redom(10)
      funcs = re.findall(self.FUNC_EXPR, string)
      for func in funcs:
            fuc = func.split('__')[1]
            fuc_name = fuc.split("(")[0]
            fuc = fuc.replace(fuc_name, fuc_name.lower())
            value = eval(fuc)
            string = string.replace(func, str(value))
      return string

def randomint(length):
    '''
    生成指定长度随机数字
    :param length:
    :return:
    '''
    s = [str(i) for i in range(10)]
    print (''.join(random.sample(s, length)))
    return ''.join(random.sample(s,length))

i=randomint(5)
print(i,type(i))
eval(randomint(5))

# eval(input())