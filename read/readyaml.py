import  yamlimport osimport jsonpathdef read(yaml_name=None,length=None,**kwargs):    # 获取当前脚本所在文件夹路径将    当前文件夹     ..    curPath = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))    # 获取yaml文件路径    yamlPath = os.path.join(curPath, "resource/"+yaml_name)    # open方法打开直接读出来    f = open(yamlPath, 'r', encoding='utf-8')    cfg = f.read()    d = yaml.load(cfg)  # 用load方法转字典    #print(d.__class__)  list列表    #value1 =d[length].get("element_info")    value2 = d[length].get("find_type")    #print(value1)    print(type(d))    return d#print(read(yaml_name="abc.yaml",length=3))#需求：写一个方法第一个参数是yaml/json文件，第二个参数是表达式，返回结果为匹配读取符合表达式的值#第一步先实现读取yaml文件返回一个string类型的字符串。yaml转换后可以是list，dict 是list和dict相互嵌套#读出的数据为list时，先用list操作方式取，如果包含dict再用get(key)方式去取#读出的数据为dict时，先用get.(key)操作。def get_v(file,*express):    with open(file ,'r',encoding='utf-8')as fy:        d=yaml.load(fy.read())        print(d)        print("-----",type(d))        #list方式去处理数据，先用list的方法区查找索引。        #le=len(d)        #v=d[le-1].get("cd2")        print("-----------")        #获得的data数据为dict，先用字典get处理数据        dlv=d.get("a").get("o")[0].get("cd")        j=jsonpath.jsonpath(d,"$.a")        print(j)get_v("y.yaml")