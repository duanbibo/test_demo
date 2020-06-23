import  pymysql

coon=pymysql.connect(host='127.0.0.1',user='root',password='123456',database='py_test',port=3306)

#创建一个游标对象 ，使用字典类型的游标将抓取的结果变为字典类型
#如果不指定游标的类型，name获取的知识一个元祖，只有属性值不展示属性名
cur=coon.cursor(cursor=pymysql.cursors.DictCursor)
query="select * from user_info"
#利用游标对象执行sql语句，游标的执行结果不能直接获取返回数据
cur.execute(query)
#需要使用fetchone()方法进行抓取执行结果
data=cur.fetchone()

#需要执行修改、更新等操作，在执行完毕需要利用数据库实例对象执行commit操作。
#最后在执行commit操作语句中包含try except 进行回滚操作
update = "UPDATE user_info  SET name = 'update' WHERE id = 1"
try:
      cur.execute(update)
      coon.commit()
except:
      coon.rollback()


print(data)