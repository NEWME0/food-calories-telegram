from typing import List
from pydantic import BaseModel

from app.api.food.serializers import FoodDetail
from app.api.activity.serializers import ActivityDetail


class FoodPage(BaseModel):
    count: int
    next: str = None
    previous: str = None
    results: List[FoodDetail]


class ActivityPage(BaseModel):
    count: int
    next: str = None
    previous: str = None
    results: List[ActivityDetail]
