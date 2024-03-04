from pydantic import BaseModel
from typing import List


class Book_validate(BaseModel):
    title: str
    author: str
    publication: str
    year: str 


class Review_validate(BaseModel):
    book_review: str
    rating: int
    book: int
