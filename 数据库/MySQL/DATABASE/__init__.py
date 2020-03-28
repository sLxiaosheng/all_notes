import MySQLdb;

def get_conn(self):
    #获取连接
    try:
        self.con = MySQLdb.connect(
            host = "localhost",
            port = 3306,
            user = "root",
            passwd = "123456",
            db = "flask_news",
            charset = 'utf8')
    except MySQLdb.Error as e:
        print("Error %d: %s" % (e.args[0], e.args[1]))
    return self.con