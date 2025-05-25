"""
使用 SQLite 数据库来保存闪卡。
为了用 Python 而不是 SQL 来处理数据库，我们需要对象关系映射器（ORM）。
SQLAlchemy 可以将 Python 类转换为关系数据库中的表，并自动将函数调用转换为 SQL 语句。

Use SQLite database to store flashcards.
To manipulate the database in Python rather than SQL, we need an Object Relational Mapper (ORM).
SQLAlchemy can convert Python classes into tables in a relational database and automatically convert function calls into SQL statements.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base


"""
创建一个数据库。请将其命名为 flashcard ：这将确保测试的正确运行.
在数据库中创建一个表，将其命名为 flashcard.db
在每个表格行中存储一个问题和答案以及一个 ID

Create a database. Please name it flashcard: this ensures tests will run correctly.
Create a table in the database and name it flashcard.db
Each row in the table should store a question, an answer, and an ID.
"""
#  1. 数据库建立连接, check_same_thread=False 标志用于Hyperskill 可以正确地测试你的项目
#  1. Establish database connection, check_same_thread=False flag allows Hyperskill to test your project correctly
engine = create_engine('sqlite:///flashcard.sqlite?check_same_thread=False')

#  2. 在数据库中创建Flashcard表。Flashcard类定义在models.py中
#  当调用 Base.metadata.create_all(engine) 时，SQLAlchemy 会遍历 Base.metadata 中注册的所有表 
#  （即所有继承自 Base 的映射类），为尚未创建的表在数据库中执行 CREATE TABLE 操作，如果存在则跳过。
#  2. Create the Flashcard table in the database. The Flashcard class is defined in models.py
#     When Base.metadata.create_all(engine) is called, SQLAlchemy iterates over all tables registered in Base.metadata
#     (i.e., all mapped classes that inherit from Base), and performs CREATE TABLE for those that don't exist yet, skipping existing tables.
Base.metadata.create_all(engine)   # type: ignore

#  3. 创建一个会话类，用于与数据库进行交互
#  3. Create a session class for interacting with the database
SessionLocal = sessionmaker(bind=engine)
