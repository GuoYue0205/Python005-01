# 6. 张三给李四通过网银转账 100 极客币，现有数据库中三张表：

# 一张为用户表，包含用户 ID 和用户名字，另一张为用户资产表，包含用户 ID 用户总资产，
# 第三张表为审计用表，记录了转账时间，转账 id，被转账 id，转账金额。

# 请合理设计三张表的字段类型和表结构；
# 请实现转账 100 极客币的 SQL(可以使用 pymysql 或 sqlalchemy-orm 实现)，张三余额不足，转账过程中数据库 crash 等情况需保证数据一致性。

from datetime import datetime
import pymysql
from sqlalchemy.orm import sessionmaker
from sqlalchemy import DateTime
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

class TransferAccounts():
    def __init__(self, conn):
        self.conn = conn

    # 参数：转账人，接收人，钱数量
    def transfer(self, transferor, receiver, money):
        try:
            # 查询转账人是否存在
            self.check_transferor_available(transferor)
            # 查询接收人是否存在
            self.check_receiver_available(receiver)
            # 查询转账人是否有足够的钱
            self.have_enough_money(transferor, money)
            # 减去转账人的钱
            self.reduce_money(transferor, money)
            # 增加接收人的钱
            self.add_money(receiver, money)
            # 将记录存储在表中
            self.records_trans(transferor, receiver, money)
            # 提交
            self.conn.commit()
        except Exception as e:
            print(f'转账失败---{e}')
            self.conn.rollback()

    def check_transferor_available(self, transferor):
        cursor = self.conn.cursor()
        try:
            sql = "select * from User where uid =  %s" % transferor
            cursor.execute(sql)
            result = cursor.fetchall()
            if not result:
                raise Exception("用户 %s 不存在" % transferor)
        finally:
            cursor.close()

    def check_receiver_available(self, receiver):
        cursor = self.conn.cursor()
        try:
            sql = "select * from User where uid =  %s" % receiver
            cursor.execute(sql)
            result = cursor.fetchall()
            if not result:
                raise Exception(f"用户 {receiver} 不存在")
        finally:
            cursor.close()

    def have_enough_money(self, transferor, money):
        cursor = self.conn.cursor()
        try:
            sql = "select * from Assets where uid =  %s and money >= %s " % (
                transferor, money)
            cursor.execute(sql)
            result = cursor.fetchall()
            if not result:
                raise Exception("转账人没有足够的钱")
        finally:
            cursor.close()

    def reduce_money(self, transferor, money):
        cursor = self.conn.cursor()
        try:
            sql = "update Assets set money = money - %s where uid = %s" % (
                money, transferor)
            result = cursor.execute(sql)
            if not result:
                raise Exception("转账人减钱失败")
        finally:
            cursor.close()

    def add_money(self, receiver, money):
        cursor = self.conn.cursor()
        try:
            sql = "update Assets set money = money + %s where uid = %s" % (
                money, receiver)
            result = cursor.execute(sql)
            if not result:
                raise Exception("接收人添加钱失败")
        finally:
            cursor.close()

    def records_trans(self, transferor, receiver, money):
        cursor = self.conn.cursor()
        try:
            sql = "insert into TransRecords (transferor_id,receiver_id,money,transdate) values(%s,%s,%s,%s)"
            result = cursor.execute(sql, (transferor, receiver, money, datetime.now()))
            if not result:
                raise Exception("转账记录入库失败")
        finally:
            cursor.close()


# 一张为用户表，包含用户 ID 和用户名字，另一张为用户资产表，包含用户 ID 用户总资产，
# 第三张表为审计用表，记录了转账时间，转账 id，被转账 id，转账金额。

Base = declarative_base()
class User(Base):
    __tablename__ = 'User'
    uid = Column(Integer, primary_key=True,unique=True)
    user_name = Column(String(50))


class Assets(Base):
    __tablename__ = 'Assets'
    uid = Column(Integer, primary_key=True,unique=True)
    money = Column(Integer)


class TransRecords(Base):
    __tablename__ = 'TransRecords'
    id = Column(Integer, primary_key=True)
    transferor_id = Column(Integer,nullable=False)
    receiver_id = Column(Integer,nullable=False)
    money = Column(Integer,nullable=False)
    transdate = Column(DateTime(), default=datetime.now(),
                       onupdate=datetime.now(),nullable=False)


def creat_Table():
    
    db_url = 'mysql+pymysql://root:guoyue19900205@127.0.0.1:3306/testdb?charset=utf8mb4'
    engine = create_engine(db_url, echo=True, encoding='utf-8')
    Base.metadata.create_all(engine)
    # 用户表插入张三李四两个用户数据
    SessionClass = sessionmaker(bind=engine)
    session = SessionClass()
    user1 = User(uid=1001,user_name='张三')
    user2 = User(uid=1002,user_name='李四')
    session.add(user1)
    session.add(user2)
    session.commit()
    # 资产表插入张三李四两个用户的资产数据
    ass1 = Assets(uid=1001,money=100)
    ass2 = Assets(uid=1002,money=100)
    session.add(ass1)
    session.add(ass2)
    session.commit()


if __name__ == '__main__':
    # 创建三张表 User Assets TransRecords
    # creat_Table()
    
    # 执行张三向李四转账100操作
    connect = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='guoyue19900205',
        db='testdb',
        charset='utf8'
    )
    
    trans = TransferAccounts(connect)

    trans.transfer(1001,1002,100)
