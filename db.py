"""
使用 SQLite 数据库来保存闪卡。
为了用 Python 而不是 SQL 来处理数据库，我们需要对象关系映射器（ORM）。
SQLAlchemy 可以将 Python 类转换为关系数据库中的表，并自动将函数调用转换为 SQL 语句。
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base


"""
创建一个数据库。请将其命名为 flashcard ：这将确保测试的正确运行.
在数据库中创建一个表，将其命名为 flashcard.db
在每个表格行中存储一个问题和答案以及一个 ID
"""
#  1. 数据库建立连接, check_same_thread=False 标志用于Hyperskill 可以正确地测试你的项目
engine = create_engine('sqlite:///flashcard.sqlite?check_same_thread=False')

#  2. 在数据库中创建Flashcard表。Flashcard类定义在models.py中
#  当调用 Base.metadata.create_all(engine) 时，SQLAlchemy 会遍历 Base.metadata 中注册的所有表 
#  （即所有继承自 Base 的映射类），为尚未创建的表在数据库中执行 CREATE TABLE 操作，如果存在则跳过。
Base.metadata.create_all(engine)   # type: ignore

#  3. 创建一个会话类，用于与数据库进行交互
SessionLocal = sessionmaker(bind=engine)




