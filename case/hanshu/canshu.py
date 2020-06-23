import clip

'''
函数的参数是比较关键的一点，当函数的参数列表是不确定的时候，内部逻辑是如何获取、处理的。

  首先要了解参数的优先级顺序：在调用函数传入实参时，是需要和形参进行一一对应的。
   def prin(x:int,z=None,y=3,*arge,d1=60,d2=80,**kwarge)->int:


'''

def  chuli(a,b=2,c=None,*args,d1,d2,**kwargs):


      if args is not None:
                print(args)
      else:
            print('pass2')

      if kwargs is not None:
            print(kwargs)


#在传参调用时，如果传入的值为单个元素，就由arge进行处理，如果是key=value带等号这种就有**kwarge进行处理
c=chuli(5,8,9,10,11,12,13,d1='v1',d2='v2',d3='v3',d4='v4')
c

#利用HTML中的标签特性，实现创建一个标签可以自定义属性。
#实现第一种： < img    class=""   src=""   title="  ">
# 实现第二种：<p   class="">  自定义消息内容</p>
def tag(name, *content, cls=None, **attrs):

      '''
      :param name: 标签名称
      :param content: 文本内容
      :param cls: class属性值
      :param attrs: 其他的属性
      :return:  HTML标签
      '''

      if cls is not None:
            attrs['class']=cls
      if  attrs:
            attr_str=" ".join('%s=%s'%(attr,value) for attr,value in attrs.items())
      else:
            attr_str=''
      if  content:
            return  ' '.join('<%s %s>%s</%s>'%(name,attr_str,c,name)for c in content)

      else:
            return  '<%s %s>'%(name,attr_str)

html1=tag('p','helloword',cls="abc")
print(html1)
html2=tag('img','hello',scr='http://ww.baidu.com')
print(html2)
