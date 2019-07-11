

''''''
'''if条件1 执行语句,elif条件2 执行语句 ,elif条件3  执行语句, else 执行语句
  可以在条件语句外面添加 try。。finally 进行每个分支都进行执行这段话
'''

'''
if 条件1，执行语句，else执行语句：
'''
strbefor="893456"
strafter="167890"
try:
  print("这俩字符是%s,%s" % (strbefor[0:2], strafter[3:5]))
  if int(strbefor[0:2])==int(strafter[3:5]):
      print("相等")
  elif int(strbefor[0:2])>int(strafter[3:5]):
      print("前面的大")
  else :
      print("后面的大")
finally:
      print("他俩之和为,%d"%(int(strbefor[0:2])+int(strafter[3:5])))