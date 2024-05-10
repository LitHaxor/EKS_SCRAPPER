from celery import Celery
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from scraper.models.base import Base
from scraper.config import DATABASE_URL, REDIS_URL

app = Celery('scraper', broker=REDIS_URL, include=['scraper.sites.imdb'], broker_connection_retry_on_startup=True)

app.conf.update(
    result_expires=3600,
)

engine = create_engine(url=DATABASE_URL)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

if __name__ == '__main__':
    app.start()
