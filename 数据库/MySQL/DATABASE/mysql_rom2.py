import MySQLdb
# ORM 链接数据库
from sqlalchemy import create_engine
# pymysql需要加上
engine = create_engine('mysql+pymysql://root:123456@localhost:3306/news?charset=utf8')
# 模型声明（声明的class 都是继承他）
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
# class需要使用到的数据类型
from sqlalchemy import Column, Integer, String, DateTime, Boolean


class News(Base):
    ''' 新闻类型 '''
    __tablename__ = 'news'
    id = Column(Integer, primary_key=True)
    #id = Column('news_id',Integer, primary_key=True) 字段名别名
    title = Column(String(200), nullable=False)
    content = Column(String(2000), nullable=False)
    types = Column(String(10), nullable=False)
    image = Column(String(300))
    author = Column(String(20))
    view_count = Column(Integer)
    created_at = Column(DateTime)
    is_valid = Column(Boolean)


# 创建表 帮我们把些sql的工作都完成了
News.metadata.create_all(engine)
# 如果报错Warning: (1366, "Incorrect string value: '\\xD6\\xD0\\xB9\\xFA\\xB1\\xEA...' for column 'VARIABLE_VALUE' at row 489") 不用管它 它是Mysql版本自带的警告 不影响建表


obj = News()
