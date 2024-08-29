from sqlalchemy import Column, Date, String, Integer
from database import Base

# database.py에서 생성한 Base import
from database import Base


# Base를 상속 받아 SQLAlchemy model 생성
class Profile(Base):
    __tablename__ = "profiles"

    user_name = Column(String, nullable=False, name="user", primary_key=True)
    name = Column(String, nullable=True)
    sex = Column(String, nullable=True)
    birth = Column(Date, nullable=True)
    mbti = Column(String, nullable=True)
    keywords = Column(String, nullable=True)
    contents = Column(String, nullable=True)


class Diary(Base):
    __tablename__ = "diary"

    id = Column(Integer, primary_key=True, index=True)  # 기본 키로 사용할 id 컬럼 추가
    date = Column(Date, nullable=True)
    keywords = Column(String, nullable=True)
    contents = Column(String, nullable=True)
    happy = Column(String, nullable=True)
    user_name = Column(String, nullable=False, name="user")