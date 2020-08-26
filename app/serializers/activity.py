from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel


class ActivityCategoryDetail(BaseModel):
    date_created: datetime
    date_modified: datetime
    title: str
    description: str = None


class ActivityCategoryCreate(BaseModel):
    title: str
    description: Optional[str] = ''


class ActivityCategoryList(BaseModel):
    __root__: List[ActivityCategoryDetail]


class ActivityDetail(BaseModel):
    date_created: datetime
    date_modified: datetime
    title: str
    description: str = None
    rating: int
    category: ActivityCategoryDetail
    energy: int


class ActivityCreate(BaseModel):
    title: str
    description: Optional[str] = ''
    category: Optional[int] = None
    energy: Optional[int] = 0


class ActivityList(BaseModel):
    __root__: List[ActivityDetail]
