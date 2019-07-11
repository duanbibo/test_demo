from  tkinter import *


#创建主窗口
win=Tk()
#设置窗口名称
win.title("计算器")
#设置窗口大小，以及边距
#win.geometry("300x300+300+20")
fr=Frame(win)
fr.pack()

'''
Label:标签控件，可以显示文本
'''
#win      父窗体
# text    显示的文本内容
#bg      背景颜色
#fg     字体颜色
#fount     字体
#width    宽度
#height   高度
#wraplength  指定text文本中指定多宽换行
#justify   设置换行后的对齐方式
#anchor    位置 n上北 s下南  c居中 en东北
label= Label(win,text="tk 的标签",
                     bg="pink",
                     fg="red",
                     font=("宋体",20),
                     width=20,
                     height=5,
                     wraplength=50,
                     anchor="c",
                     justify="left",
                     )
label.pack()
#显示出现
#
#
# '''
# Button 按钮控件
#
# '''
#
# def func():
#       print("i am  button")

#创建按钮,按钮的窗口，名称,绑定事件函数   command=func,不带括号
button1=Button(win,text="打印",width=4,height=1)
button1.pack()

button2=Button(win,text="退出",command=win.quit)
button2.pack()

''' 
Entry 输入控件： 用于显示简单的文本内容
show="*" 将输入的文本替换展示， 相当于密文
e=tkinter.Variable()  #创建个变量
textvariable=e  绑定个变量
'''
e=Variable()  #创建个变量 ,
entry=Entry(win,textvariable=e)  #把这个变量写入文本内容

e.set("saga")# 设置输入框的值，进行赋值
entry.get()# 获取输入框的值
entry.pack()

'''
Text 文本控件，用于显示多行文本
   text.insert(tkinter.INSERT,str)  #插入文本
  由于多行文本有可能超出内容，需要在右侧添加滚动条
  s=tkinter.Scrollbar() 添加滚动条
'''
#创建滚动条
scroll=Scrollbar()
#创建多行文本
text=Text(win,width=30,height=4)
#设置滚动条在文本右侧，fill填充满
scroll.pack(side=RIGHT,fill=Y)
text.pack(side=LEFT,fill=Y)
#将右侧滚轴和文本输入框关联起来，做到拖动滚轴/文本时，对方同步展示;
scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)

str='''Traceback (most recent call last):
  File "tkinter.py", line 4, in <module>
    import tkinter
  File "C:\haoyue.hu\Desktop、tkinter.py", line 5, in <module>
    top = tkinter.Tk()
AttributeError: module 'tkinter' has no attribute  '''

text.insert(INSERT,str)

'''
checkbutton 多选框
'''




'''
需求：做1个按钮和文本框，
实现点击按钮后，文本框的值输出到控制台中
结果：Pass
'''
# def showinfo():
#       print(entrya.get())
#
# entrya=tkinter.Entry(win)
# entrya.pack()
#
# bon=tkinter.Button(win,text="打印",command=showinfo)
# bon.pack()



'''
需求：做一个按钮和2个文本框，
实现在第一个文本框输入值后，点击按钮，将值赋予第二个文本框内
结果：fail

'''
# def showinfo():
#       return entry0.get()
#
# entry0=tkinter.Entry(win)
# entry0.pack()
#
# new=tkinter.Variable()
# new.set(showinfo())
#
# button0=tkinter.Button(win,text="输出",command=showinfo)
# button0.pack()
#
# entry00=tkinter.Entry(win,textvariable=new)
# entry00.pack()



'''
 需求：做3个文本框1个按钮
 实现在前2个文本框内输入值，点击按钮求他俩的和
 结果：fail
'''

# def one():
#       return entry1.get()
# def  two():
#       return entry2.get()
# def funsum():
#       return entry1.get()+entry2.get()
# entry1=tkinter.Entry(win,)
# entry2=tkinter.Entry(win,)
# entrysum=tkinter.Entry(win,textvariable=funsum())
#
# buttosum=tkinter.Button(win,text="求和",command=funsum)
# buttosum.pack()
# entry1.pack()
# entry2.pack()
# entrysum.pack()










#进入消息循环
win.mainloop()