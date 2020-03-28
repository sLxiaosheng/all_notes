import MySQLdb

try:
    # 建立连接
    con = MySQLdb.connect(
        # 交代数据库的属性
        host='localhost',
        user='root',
        passwd='123456',
        #数据库的名字为schooldog
        db= 'schooldog',
        port=3306,
        charset='utf8'
    )
    if con:
        print("数据库存在，不为空")
    cursor = con.cursor()
    # 查询语句   schooldog 为表名字
    cursor.execute('SELECT * FROM schooldog ORDER BY ID DESC;')
    # 接受结果
    rest = cursor.fetchone()
    # 打印结果
    print(rest)
#输出异常
except MySQLdb.Error as e:
    print("Error %d: %s" % (e.args[0], e.args[1]))

#关闭连接
con.close()