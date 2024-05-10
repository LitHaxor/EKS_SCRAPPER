from sqlalchemy import Column, String, Integer, DateTime
from scraper.models.base import BaseModel

class Movie(BaseModel):
    __tablename__ = 'movies'

    title = Column(String)
    year = Column(Integer)
    director = Column(String)
    stars = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
