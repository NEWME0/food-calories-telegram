from typing import List
from datetime import datetime
from pydantic import BaseModel
from app.serializers.food import FoodDetail
from app.serializers.activity import ActivityDetail


class FoodJournalDetail(BaseModel):
    food: FoodDetail
    weight: int
    datetime: datetime


class FoodJournalList(BaseModel):
    __root__ = List[FoodJournalDetail]


class FoodJournalCreate(BaseModel):
    date_created: datetime
    date_modified: datetime
    food: int
    weight: int
    datetime: datetime


class ActivityJournalDetail(BaseModel):
    activity: ActivityDetail
    duration: int
    datetime: datetime


class ActivityJournalList(BaseModel):
    __root__ = List[FoodJournalDetail]


class ActivityJournalCreate(BaseModel):
    date_created: datetime
    date_modified: datetime
    activity: int
    duration: int
    datetime: datetime
