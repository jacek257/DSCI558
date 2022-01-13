# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CastItem(scrapy.Item):
    id = scrapy.Field()
    url = scrapy.Field()
    timestamp_crawl = scrapy.Field()
    name = scrapy.Field()
    movies = scrapy.Field()
