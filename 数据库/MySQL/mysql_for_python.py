import MySQLdb

#封装
class MysqlSearch(object):

    def __init__(self):
        #执行程序
        self.get_conn();

    def get_conn(self):
        try:
            # 建立连接
            self.conn = MySQLdb.connect(
                # 交代数据库的属性
                host='localhost',
                user='root',
                passwd='123456',
                #数据库名称
                db='news',
                port=3306,
                charset='utf8'
            )
            if self.conn:
                print("数据库存在，不为空")

            #创建游标
            cursor = self.conn.cursor()

            #执行sql语句
            cursor.execute('SELECT * FROM news ORDER BY title DESC;')
            #读取一行数据，  取回一行
            rest = cursor.fetchone()
            #打印结果
            print(rest)
        except MySQLdb.Error as e:
            print("Error %d: %s" % (e.args[0], e.args[1]))

    def close_conn(self):
        try:
            if self.conn:
                # 关闭链接
                self.conn.close()
        except MySQLdb.Error as e:
            print('Error: %s' % e)

    def get_one(self):
        #准备SQL
        sql = 'SELECT * FROM news WHERE title = %s ORDER BY title DESC;'
        #找到cursor
        cursor = self.conn.cursor()
        #执行
        cursor = cursor.execute(sql, ('APPLE',))
        #拿到结果
        rest = dict(zip([k[0]] for k in cursor.description), cursor.fetchone())

        #关闭cursor，链接
        cursor.close()
        #self.close_conn()
        return rest

    def get_more(self):
        #准备SQL
        sql = 'SELECT * FROM news WHERE title = %s ORDER BY title DESC;'

        #找到cursor
        cursor = self.conn.cursor()
        #执行
        cursor.execute(sql, ('APPLE',))
        #拿到结果,以字典的形式保存
        rest = [dict(zip([k[0] for k in cursor.description], row)) for row in cursor.fetchall()]

        #关闭cursor，链接
        cursor.close()
        #self.close_conn()
        return rest

    def get_all(self):
        cursor = self.conn.cursor()
        sql = 'SELECT * FROM news WHERE id = %s;'
        i = 0;
        sql1 = 'SELECT * FROM news WHERE id = i'
        rest = cursor.execute(sql, (str(i),))

        while True:
            i += 1
            rest = cursor.execute(sql, (str(i), ))
            rest = cursor.fetchone()
            if rest:
                print(rest)
            else:
                break

        cursor.close()
        self.conn.close()

    def get_more_by_page(self, page, page_size):
        #分页查询
        offset = (page - 1) * page_size
        sql = 'SELECT * FROM news WHERE types = %s ORDER BY create_at DESC LIMIN offset, page_size'
        cursor = self.conn.cursor()
        cursor.execute(sql, ('FRUITS', offset, page_size))
        rest = [dict(zip([k[0] for k in cursor.description], row) for row in cursor.fetchall())]

        cursor.close()
        self.close_conn()
        return rest

    def add_one(self):
        row_count = 0

        try:
            sql = (
            "INSERT INTO `news`(`title`, `image`, `content`, `types`, `is_vaild`) VALUE"
            "(%s, %s, %s, %s, %s);"
            )
            #获取链接和cursor
            cursor = self.conn.cursor()
            cursor.execute(sql, ('标题1', 'lkdfjlaj', '新闻内容1', '推荐', 10))
            #提交事务
            self.conn.commit()
            #关闭cursor和链接
            cursor.close()
            self.close_conn()
        except MySQLdb.Error as e:
            print("Error %d: %s" % (e.args[0], e.args[1]))
            # 回滚事务
            self.conn.rollback()
        # 执行最后一条SQL影响的行数
        row_count = cursor.rowcount
        # 关闭cursor和链接，一定要先关游标，再关链接
        cursor.close()
        self.close_conn()
        # row_count > 0 表示成功
        return row_count > 0

    def add_ones(self):
        ''' 插入数据 '''
        # 受影响的行数
        row_count = 0
        try:
            # 准备SQL
            sql = (
                "INSERT INTO `news`(`title`,`image`, `content`, `types`, `is_valid`) VALUE"
                "(%s, %s, %s, %s, %s);"
            )
            # 获取链接和cursor
            cursor = self.conn.cursor()
            # 执行sql
            # 提交数据到数据库
            cursor.execute(sql, ('标题11', '/static/img/news/01.png', '新闻内容5', '推荐', 1))
            # cursor.execute(sql, ('标题12', '/static/img/news/01.png', '新闻内容6', '推荐', 1))
            # 提交事务
            self.conn.commit()
        except :
            print('error')
            # 回滚事务
            self.conn.rollback()
        # 执行最后一条SQL影响的行数
        row_count = cursor.rowcount
        # 关闭cursor和链接,  一定要先关游标，再关链接
        cursor.close()
        self.close_conn()
        # row_count > 0 表示成功
        return row_count > 0

def main():
    obj = MysqlSearch()
    rest = obj.get_more()
    #print(rest)

    print("~~~~~~~~~~")
    obj1 = MysqlSearch()
    rest = obj1.get_all()

    #print('~~~~~~')
    #obj2 = MysqlSearch()
    #print(obj2.get_more_by_page(2,2))

    print('~~~~~~~~')
    obj3 = MysqlSearch()
    print(obj3.add_one())

    print("~~~~~~~~~~")
    obj1 = MysqlSearch()
    rest = obj1.get_all()


if __name__ == '__main__':
    main()