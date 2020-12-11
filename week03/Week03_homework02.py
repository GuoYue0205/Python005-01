# 2. 使用 sqlalchemy ORM 方式创建如下表，使用 PyMySQL 对该表写入 3 条测试数据，并读取:
# 用户 id、用户名、年龄、生日、性别、学历、字段创建时间、字段更新时间
# 将 ORM、插入、查询语句作为作业内容提交

import pymysql
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import DateTime


# 使用sqlalchemy创建表
Base = declarative_base()


class User(Base):
    __tablename__ = 'User'
    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(50), index=True)
    user_age = Column(Integer)
    user_birthday = Column(String(50))
    user_sex = Column(String(10), index=True)
    user_education = Column(String(50), index=True)
    create_time = Column(DateTime(), default=datetime.now)
    update_time = Column(DateTime(), default=datetime.now,
                         onupdate=datetime.now)


def creat_UserTable():
    db_url = 'mysql+pymysql://root:guoyue19900205@127.0.0.1:3306/testdb?charset=utf8mb4'
    engine = create_engine(db_url, echo=True, encoding='utf-8')
    Base.metadata.create_all(engine)


# 使用pymysql插入数据
def write_UserTable(values):
    try:
        with connect.cursor() as cursor:
            sql = 'INSERT INTO User (user_name,user_age,user_birthday,user_sex,user_education) VALUES (%s,%s,%s,%s,%s)'
            cursor.executemany(sql, values)  # 游标插入多行数据
        connect.commit()
    except Exception as e:
        print(f'写入数据错误--{e}')
    finally:
        print(cursor.rowcount)  # 打印sql生效行数

# 查询表数据


def read_UserTable():
    try:
        # 建立一个游标对象cursor
        with connect.cursor() as cursor:
            sql = 'SELECT * from User'
            # 使用execute 方法执行sql
            cursor.execute(sql)
            # 取结果当中的一行，赋值result
            result = cursor.fetchall()
            print(result)
    except Exception as e:
        print(e)
    finally:
        print('读取结束')


if __name__ == '__main__':
    # 创建
    creat_UserTable()

    connect = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='guoyue19900205',
        db='testdb',
        charset='utf8'
    )
    # 插入
    values = (
                ('张三', 20, '2000-01-01', '男', '小学肄业'),
                ('李四', 30, '1990-01-02', '男', '大学本科'),
                ('王五', 40, '1980-01-03', '男', '博士')
            )
    write_UserTable(values)
    # 查询
    read_UserTable()
