import MySQLdb

#建立连接
con = MySQLdb.connect(
    #交代数据库的属性
    host = 'localhost',
    user = 'root',
    passwd = '123456',
    db = 'news',
    port = 3306,
    charset = 'utf8'
)
cursor = con.cursor()
cursor.execute('SELECT * FROM ‘news‘ ORDER BY ’created_at‘ DESC;')
rest = cursor.FETCHONE()
print(rest)

#关闭链接
con.close()



