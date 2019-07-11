import tkinter
from tkinter import ttk


#创建主窗口
win=tkinter.Tk()
#设置窗口名称
win.title("计算器")
#设置窗口大小，以及边距
#win.geometry("300x300+300+20")


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
# label= tkinter.Label(win,text="tk 的标签",
#                      bg="pink",
#                      fg="red",
#                      font=("宋体",20),
#                      width=20,
#                      height=5,
#                      wraplength=50,
#                      anchor="c",
#                      justify="left",
#                      )
# label.pack()
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
button1=tkinter.Button(win,text="打印",width=4,height=1)
button1.pack()

button2=tkinter.Button(win,text="退出",command=win.quit)
button2.pack()

''' 
Entry 输入控件： 用于显示简单的文本内容
show="*" 将输入的文本替换展示， 相当于密文
e=tkinter.Variable()  #创建个变量
textvariable=e   # 绑定个变量
'''
e=tkinter.Variable()  #创建个变量 ,
entry=tkinter.Entry(win,textvariable=e)  #把这个变量写入文本内容

e.set("saga")# 设置输入框的值，进行赋值
entry.get()# 获取控件内容的值
entry.pack()

'''
Text 文本控件，用于显示多行文本
   text.insert(tkinter.INSERT,str)  #插入文本
  由于多行文本有可能超出内容，需要在右侧添加滚动条
  s=tkinter.Scrollbar() 添加滚动条
'''
#创建滚动条
scroll=tkinter.Scrollbar()
#创建多行文本
text=tkinter.Text(win,width=30,height=4)
#设置滚动条在文本右侧，fill填充满
scroll.pack(side=tkinter.RIGHT,fill=tkinter.Y)
text.pack(side=tkinter.LEFT,fill=tkinter.Y)
#将右侧滚轴和文本输入框关联起来，做到拖动滚轴/文本时，对方同步展示;
scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)

str='''Traceback (most recent call last):
  File "tkinter.py", line 4, in <module>
    import tkinter
  File "C:\haoyue.hu\Desktop、tkinter.py", line 5, in <module>
    top = tkinter.Tk()
AttributeError: module 'tkinter' has no attribute  '''

text.insert(tkinter.INSERT,str)

'''
checkbutton 多选框
 
 需求：将选中的复选框的值打印出来到文本框内
  思想：先将每个复选框绑定个变量，这个变量为布尔值true或者false
       判断，如果复选框为true时，先清除文本输入框的内容，
       再讲全部勾选的复选框的值放入 文本输入框。
  核心：通过绑定布尔值的变量值，获取勾选状态，然后再操作
       
'''
def update():
      message=""
      if hobby1.get()==True:
            message+="money\n"
      if hobby2.get()==True:
            message+="pepple\n"
      text1.delete(0.0,tkinter.END)   #清空文本框的内容，从左上角到最后
      text1.insert(tkinter.INSERT, message)

hobby1=tkinter.BooleanVar()#绑定个变量 这个值为布尔值
check1=tkinter.Checkbutton(win,text="money",variable=hobby1,command=update)

hobby2=tkinter.BooleanVar()#绑定个变量布尔值
check2=tkinter.Checkbutton(win,text="people",variable=hobby2,command=update)
check1.pack()
check2.pack()

text1=tkinter.Text(win,width=30,height=4)
text1.pack()

'''
Radiobutton单选框
  实现思想：通过单选框的内的属性值为同一个为一组，绑定个统一的变量。
'''
def showradio():
      print(r.get())


r=tkinter.IntVar()
radio1=tkinter.Radiobutton(win,text="man",value=1,variable=r,command=showradio)
radio2=tkinter.Radiobutton(win,text="men",value=2,variable=r,command=showradio)

radio1.pack()
radio2.pack()

'''
combobox下拉控件
 获取下拉控件的值： 控件名字.get
'''
cv=tkinter.StringVar()
com=ttk.Combobox(win,textvariable=cv)

com.pack()
#设置下拉数据
com["value"]=("黑龙江","吉林","长春")
#设置默认值,根据下标
com.current(2)

#绑定事件,让进行操作控件时有输出函数
def func(event):
    #  print(com.get()) 可以直接获取下拉控件的值
      print(cv.get())
com.bind("<<ComboboxSelected>>",func)

'''
Frame 控件：在屏幕上显示一个矩形区域，作为容器控件
'''
frm=tkinter.Frame(win)
frm.pack()
#left
frm_1=tkinter.Frame(frm)
tkinter.Label(frm_1,text="左上",bg="pink").pack(side=tkinter.TOP)
tkinter.Label(frm_1,text="左上",bg="pink").pack(side=tkinter.TOP)

'''
 Spinbox数值范围控件  类似于闹钟的时间
    默认步长1

'''
v = tkinter.StringVar()
sp = tkinter.Spinbox(win, from_=0, to=100, increment=1, textvariable=v)

sp.pack(fill=tkinter.Y, side=tkinter.LEFT)

'''
鼠标点击事件：绑定个元素的时间，当鼠标操作这个任意元素的时候进行相应方法
           声明的函数：
           声明的元素：
       语法 元素.bind("<类型-int>",func)
       


'''

def func(event):
      print(event.x,event.y)
but1=tkinter.Button(win,text="mouse click")
but1.bind("<Button-1>",func)
but1.pack()

'''
listbox 列表文本
Menu    顶层菜单
Treeview  表格数据

'''

'''
绝对布局：窗口的变化对位置没有影响
label.place(x=10,y=10) x.y与左上角的距离
相对布局：窗体改变对控件有影响【手动控制缩放扩大影响】
label.pack(fill=tkinter.Y,side=tkinter.LEFT)
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
结果：pass
过程：1.声明个空的文本框 2.创建个按钮 ，执行函数命令 3创建个空的文本框，文本框的值为一个变量  4.声明个变量，为第二个文本框的值
     5. 函数中 返回变量的值进行指向 第一个空文本框内的值
执行排顺序： 1 -5 -2-3-4    在python语言内一定要注意顺序

'''

entry0=tkinter.Entry(win)
entry0.pack()

def showinfo():
      return new.set(entry0.get())

button0=tkinter.Button(win,text="输出",command=showinfo)
button0.pack()

new=tkinter.Variable()  #创建个变量
entry1=tkinter.Entry(win,textvariable=new )

entry1.pack()




'''
 需求：做3个文本框1个按钮
 实现在前2个文本框内输入值，点击按钮求他俩的和
 结果：pass
'''

entry1=tkinter.Entry(win)
entry2=tkinter.Entry(win)

def funsum():
      return sum.set(int(entry1.get())+int(entry2.get()))


buttosum=tkinter.Button(win,text="求和",command=funsum)
buttosum.pack()

sum=tkinter.Variable()
entrysum=tkinter.Entry(win,textvariable=sum)



entry1.pack()
entry2.pack()
entrysum.pack()










#进入消息循环
win.mainloop()