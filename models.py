#  注意：sqlalchemy 2.0 使用 sqlalchemy.orm 导入 declarative_base。本项目使用的是 sqlalchemy 1.3.x
#  Note: sqlalchemy 2.0 imports declarative_base from sqlalchemy.orm. This project uses sqlalchemy 1.3.x
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


# 在数据库中创建表，以便 declarative_base() 函数可以建立基类。
# 基类存储了声明系统中的类目录和映射表。一旦基类被声明，我们可以在其中定义任意数量的映射类。
# Create tables in the database so that the declarative_base() function can establish a base class.
# The base class stores the class registry and mapping tables for the declarative system. 
# Once the base is declared, we can define any number of mapped classes in it.
Base = declarative_base()

# 我们希望在数据库中存储答案和问题。为此，我们需要定义以下类：
# We want to store answers and questions in the database. To do this, we need to define the following class:
class FlashCard(Base):
    # 声明式形式的类必须有一个 __tablename__ 属性，并且至少有一个 Column 构成主键。
    # Declarative-style classes must have a __tablename__ attribute, and at least one Column as the primary key.
    __tablename__ = 'flashcard'

    id = Column(Integer, primary_key=True)
    question = Column(String)
    answer = Column(String)
    rep_count = Column(Integer, default=1)

