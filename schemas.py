from typing import List, Union
from pydantic import BaseModel
from datetime import date

# ProfileBase 생성
class ProfileBase(BaseModel):
    user_name: str
    name: Union[str, None] = None
    sex: Union[str, None] = None
    birth: Union[date, None] = None
    mbti: Union[str, None] = None
    keywords: Union[str, None] = None
    contents: Union[str, None] = None

# ProfileCreate 생성 (ProfileBase 상속)
class ProfileCreate(ProfileBase):
    pass

# API에서 데이터를 읽을 때/반환할 때 사용될 모델
class Profile(ProfileBase):
    class Config:
        from_attributes = True

# DiaryBase 생성
class DiaryBase(BaseModel):
    date: Union[date, None] = None
    keywords: Union[str, None] = None
    contents: Union[str, None] = None
    happy: Union[str, None] = None
    user_name: str

# DiaryCreate 생성 (DiaryBase 상속)
class DiaryCreate(DiaryBase):
    pass

# API에서 데이터를 읽을 때/반환할 때 사용될 모델
class Diary(DiaryBase):
    class Config:
        from_attributes = True
