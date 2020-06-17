import pymysql




#建立数据库连接
coon=pymysql.connect(
      host="172.16.10.57:65432",
      user="postgres",
      password="dev",
      database="test_un",
      charset="utf8"
)
#获取游标
cursor=coon.cursor()

# # 定义要执行的SQL语句
# sql = "CREATE TABLE USER1 (id INT auto_increment PRIMARY KEY ,name CHAR(10) NOT NULL UNIQUE,age TINYINT NOT NULL)ENGINE=innodb DEFAULT CHARSET=utf8;"
#
#
# cursor.execute(sql)
#
# cursor.close()
# coon.close()