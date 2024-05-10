import scrapy
from scraper.celery import app, Session
from scraper.models.movie import Movie
from scrapy import Request
from datetime import datetime

@app.task
def process_movie(title, year, director, stars):
    try:
        print("Processing movie:", title)
        session = Session()
        movie = None
        if session.query(Movie).filter(Movie.title == title).count() > 0:
            movie = session.query(Movie).filter(Movie.title == title).first()
            movie.year = year
            movie.director = director
            movie.stars = stars
            movie.updated_at = datetime.now()
        else:
            movie = Movie(title=title, year=year, director=director, stars=stars, created_at=datetime.now(), updated_at=datetime.now())
        session.add(movie)
        session.commit()
        session.close()
    except Exception as e:
        print(f"Error in processing movie callback: {e}")



class IMDbSpider(scrapy.Spider):
    name = "imdb"
    baseUrl = 'https://www.imdb.com'
    start_urls = ['https://www.imdb.com/chart/top/']

    def parse(self, response):
        try:
            lists = response.css('ul.ipc-metadata-list').xpath('./li')
            print(f"Found {len(lists)} movies")

            for movie_link in lists:
                title_link = movie_link.css('a').xpath('@href').get()
                full_link = self.baseUrl + title_link
                yield response.follow(full_link, self.parse_movie)
        except Exception as e:
            print(f"Error in parsing IMDb page: {e}")

    def parse_movie(self, response):
        try:
            print(f"Processing movie page: {response.url}")
            title = response.xpath('normalize-space(//h1/span/text())').get()
            year = response.xpath('normalize-space(.//ul[contains(@class, "ipc-inline-list")]/li/a[contains(@href, "releaseinfo")]/text())').get()
            director = response.css('.ipc-metadata-list-item__list-content-item--link::text').get()
            stars = response.xpath('//div[@data-testid="hero-rating-bar__aggregate-rating__score"]/span/text()').get()
            print(f"Title: {title}, Year: {year}, Director: {director}, Stars: {stars}")
            process_movie.delay(title, year, director, stars)
        except Exception as e:
            print(f"Error in parsing movie page: {e}")
