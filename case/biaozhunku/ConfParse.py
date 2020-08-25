import configparser


'''
configparser : 用来解析配置文件的，
   关键概念： section节点，文件中通过【sectionName】 划分上下文，文件中需要配置个[DEFAULT]默认的节点
            查找是通过 get('sectionName','key') 进行查找的，
            如果指定的命名空间查不到会去默认的命名空间里面找。
            对于布尔类型的值，内部调用 getboolean('sectionName','key' )查找，
            并且将1，ON，true内部进行了转换为True; 0,off ,false 转换了False
            对于其他不符合的数据，会报valueError
            
            如果把这些机制全部用上，那么配置项值的查找规则如下：
            1）如果找不到节名，就抛出NoSectionError。
            2）如果给定的配置项出现在get()方法的vars参数中，则返回vars参数中的值。
            3）如果在指定的节中含有给定的配置项，则返回其值。
            4）如果在[DEFAULT]中有指定的配置项，则返回其值。
            5）如果在构造函数的defaults参数中有指定的配置项，则返回其值。
            6）抛出NoOptionError。
            

'''

conf=configparser.ConfigParser()
conf.read('conf.conf',encoding='utf-8')

print(conf.get('section1','name'))
print(conf.get('section1','age'))
print(conf.getboolean('section1','sex')) #打印布尔值

'''
 通过将 deafult出设置模板并且格式化字符串，配置名称可以引用其他的配置名
'''
print(conf.get('db1','conn_str'))