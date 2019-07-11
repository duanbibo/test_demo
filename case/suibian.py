#coding=utf-8
import sqlite3
import sys




# list1=[7,7,7,8,8,8]
# b=[ i if i%2==1 else i+5 for i in  list1  ]
# c=[m + n for m in 'ABC' for n in 'XYZ']
# print(c)
#
# mn=[]
# for m in 'ABC':
#       for n in 'XYZ':
#             mn.append(m+n)
# print(mn)
#
# c=10
# w=20
# e=20
# if  not  e<c :
#       print(c)
# else:
#       print("erro")
# connt=sqlite3.connect('testDb')
# connt.text_factory = str
# cur=connt.cursor()
# cur.execute('create table user2 (id varchar(20) primary key, name varchar(20))')
# cur.execute('insert into user (id, name) values (\'8\', \'Michael\')')
# cur.execute('select * from user where name=?', ('Michael',))
# values = cur.fetchall()
# print(values)
# # 关闭Cursor:
# cur.close()
# connt.commit()
# connt.close()
#!/usr/bin/env python
#coding=utf-8




# def  crelist(name1,name2,name3):
#       '''实现创建列表'''
#       global list2
#       list2=[]
#       for i in(name1,name2,name3):
#         list2.append(i)
#       return  print(list2)
# crelist(1,2,3)
#
# def selist(list1,name):
#       '''实现根据列表的名称去查找'''
#       for i in range(0,list1.__len__()-1):
#           if list2[i]==name:
#             print(i)
#
# selist(list2,3)

list2=[1,2,3,4,5,6,7]
def inlist(list1,ind,value):
      '''手写列表插入'''
      list3=list1.copy()
      a=list3.__len__()

      for i in(0,a):
         for n in(0,ind+1):
            list3[n]=list1[n]
         if n ==ind:
            list3[n+1]=value
         else:
           list3[n]=list1[n-1]
      print(list3)



inlist(list2,1,111)
print(inlist.id)


