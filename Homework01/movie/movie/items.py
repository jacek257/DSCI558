# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class MovieItem(scrapy.Item):
    # define the fields for your item here like:
    id = scrapy.Field()
    url = scrapy.Field()
    timestamp_crawl = scrapy.Field()
    title = scrapy.Field()
    director = scrapy.Field()
    cast = scrapy.Field()
    genres = scrapy.Field()
    release_date = scrapy.Field()
