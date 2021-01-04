import mysql.connector as sq

con = sq.connect(host='localhost', user='py', passwd='python123', database='test')

if con.is_connected():
    print('Connected.')
else:
    print('Err Occurred')

cursor = con.cursor()
#cursor.execute("create table sample10(id int,name varchar(10));")
#cursor.execute("insert into sample10(id, name) values({},'{}');".format(1,'abc'))

#cursor.execute("update sample10 set id=2 where name ='abc';")
#con.commit()
cursor.execute("select * from sample10")
page = cursor.fetchmany(2)

for row in page:
    print(row)
