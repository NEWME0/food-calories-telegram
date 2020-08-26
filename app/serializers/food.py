from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel


class FoodPortionDetail(BaseModel):
    date_created: datetime
    date_modified: datetime
    title: str
    description: str
    weight: int


class FoodPortionList(BaseModel):
    __root__: List[FoodPortionDetail]


class FoodPortionCreate(BaseModel):
    title: str
    description: Optional[str]
    weight: int


class FoodCategoryDetail(BaseModel):
    date_created: datetime
    date_modified: datetime
    title: str
    description: str


class FoodCategoryList(BaseModel):
    __root__: List[FoodCategoryDetail]


class FoodCategoryCreate(BaseModel):
    title: str
    description: Optional[str]


class FoodDetail(BaseModel):
    date_created: datetime
    date_modified: datetime
    rating: int
    title: str
    description: str = None
    category: FoodCategoryDetail
    portions: List[FoodPortionDetail]
    energy: int
    protein: float
    carbohydrate: float
    fat: float
    fiber: float
    sugar: float
    salt: float


class FoodList(BaseModel):
    __root__: List[FoodDetail]


class FoodCreate(BaseModel):
    title: str
    description: Optional[str] = ''
    category: Optional[int]
    portions: Optional[List[int]] = []
    energy: Optional[int]
    protein: Optional[float]
    carbohydrate: Optional[float]
    fat: Optional[float]
    fiber: Optional[float]
    sugar: Optional[float]
    salt: Optional[float]
