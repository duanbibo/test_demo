import  sys
import time
'''显示出python所有的内建函数【内嵌的函数】'''
print(dir(__builtins__))
'''

新建对象后，对象都有一个唯一的身份标识自己ID，对象一旦建立，ID永远不会改变。
如果对象的类型被改变。如从list变为tuple,那么对象的ID和类型就变了。以前的ID将会被收回。
引用计数器：此对象再被调用，如被方法使用、对象再次改变、或者去给其他变量赋值时，这个引用计数属性值就会加1

'''

a=[1,2,3]
print(id(a),type(a),sys.getrefcount(a))
a.append(4)
time.sleep(1)
a=tuple(a)

print(a,id(a),type(a),sys.getrefcount(a))
b=a
print(id(a))
print(sys.getrefcount(a),id(a),type(a))

''' 对象的属性值：获取对象的所有属性，判断对象是否具有当前的方法，获取对象当前的方法值'''
print(list.__dict__)
print(len(a))
c=[1,2,3]
print(type(c))
print(hasattr(c,"count"))
print(getattr(c,"reverse"))
print(c.pop(1))

