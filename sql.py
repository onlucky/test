
import pymysql
import time

# 打开数据库连接
db = pymysql.connect("localhost","hmx","123","apple" )

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("show tables")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchall()

for value in data:
    name=value[0]
    print ("all tables : %s " % name)

# 关闭数据库连接
db.close()

print("sleep 2")
time.sleep(2)

db=pymysql.connect("localhost","hmx","123","apple")
print("con")
cursor=db.cursor()
dropsql="drop table if exists  user"
cursor.execute(dropsql)
print("drop table")
sql="""create table user
( id int(10) not null auto_increment,
  name varchar(100),
  primary key (id)
)"""
cursor.execute(sql)

print("create talbe")
insql="insert into user values (null,'hmx')"
upsql="update user set name='root' where id=1"
sesql="select * from user"
desql="delete from user where name='hmx'"
try:
    for i in range(1,20):
        cursor.execute(insql)
    cursor.execute(insql)
    cursor.execute(upsql)
    cursor.execute(sesql)
    results=cursor.fetchall()
    print(results)
    n=cursor.execute(desql)
    print("n:",n)
    db.commit()
    cursor.execute(sesql)
    print(results)
    #print(cursor.fetchall())
    # cursor.execute(sesql)
except:
    db.rollback()
    print("111")

cursor.execute(sesql)
results=cursor.fetchall()
for row in results:
    uid=row[0]
    name=row[1]
    print("uid:name",uid,name)
db.close()