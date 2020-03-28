from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
#引入session对象
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, DateTime, Boolean

#创建连接
engine = create_engine("mysql://root:123456@localhost:3306/news?charset=utf8")

Session = sessionmaker(bind=engine)

#基类
Base = declarative_base()

#继承与Base类
class News(Base):
    ''' 新闻类型 '''
    #表名
    __tablename__ = 'news'
    #id  与定义主键
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    content = Column(String(2000), nullable=False)
    types = Column(String(10), nullable=False)
    image = Column(String(300))
    author = Column(String(20))
    view_count = Column(Integer)
    created_at = Column(DateTime)
    is_valid = Column(Boolean)


class MysqlOrmTest(object):

    def __init__(self):
        self.session = Session()

    def add_one(self):
        ''' 添加数据 '''
        new_obj = News(
            title='ORM标题',
            content='content',
            types="百家"
        )
        #通过session 来传递，控制数据库，与cursor游标类似
        self.session.add(new_obj)
        #提交
        self.session.commit()
        return new_obj

    def get_one(self):
        ''' 获取一条数据 '''
        #query(表名字).get(第几行的数据)
        return self.session.query(News).get(3)

    def get_more(self):
        ''' 获取多条数据 '''
        return self.session.query(News).filter_by(is_valid=1)

    def update_data(self):
        ''' 修改数据 '''
        obj = self.session.query(News).get(3)
        if obj:
            #改变默认值为0
            obj.is_valid = 0
            self.session.add(obj)
            self.session.commit()
            return True
        return False

    def update_all(self):
        #  filter_by 条件筛选
        data_list = self.session.query(News).filter_by(is_valid = 1)
        for item in data_list:
            item.is_vaid = 3
            self.session.add(item)
        self.session.commit()

    def delete_data(self):
        ''' 删除数据 '''
        # 获取要删除的数据
        data = self.session.query(News).get(39)
        self.session.delete(data)
        self.session.commit()


def main():

    obj = MysqlOrmTest()
    rest = obj.add_one()
    print(rest.id)

    rest = obj.get_one()
    if rest:
        print('ID: {0} => {1}'.format(rest.id, rest.title))
    else:
        print('Not exist.')
    # print(obj.get_one().title)

    # print(obj.get_more().count())
    # for row in obj.get_more():
    #     print(row.title)

    rest = obj.update_data()
    print(obj.update_data())

    rest = obj.update_all()
    #print(rest.is_valid)

    #obj.delete_data()



if __name__ == '__main__':
    main()