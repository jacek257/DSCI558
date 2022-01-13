# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 13:48:09 2021

@author: Jimi
"""

from bs4 import BeautifulSoup as soup

import scrapy
from bios.items import BiosItem

class BiosSpider(scrapy.Spider):
    name = "bios"
    
    allowed_domains = ['imdb.com']
    start_urls = ['https://www.imdb.com/search/name/?birth_monthday=06-29&start={}&ref_=rlm'.format(idx) for idx in range(1, 550, 50)]
    
    def parse(self, response):
    
        page_soup = soup(response.body, 'html.parser')
        
        for item in page_soup.select(".lister-item-header"):
            person_link = "https://www.imdb.com" + item.select('a')[0]['href']
            yield scrapy.Request(person_link, callback=self.get_deatils)
        
    def get_deatils(self, response):
        
        page_soup = soup(response.body, 'html.parser')
        
        try:
            more = page_soup.find('span', class_="see-more inline nobr-only")
            details_link = "https://www.imdb.com" + more.select('a')[0]['href']
            yield  scrapy.Request(details_link, callback=self.parse_details)
        except:
            self.logger.info('Has no biography {}'.format(response.url))
    
    def parse_details(self, response):
        
        page_soup = soup(response.body, 'html.parser')
        
        bio_tag = page_soup.select('a[name="mini_bio"]')[0]
        # the first sibling is an h4 tag
        bio = bio_tag.find_next_sibling().find_next('p').text.strip()
        
        bio_item = BiosItem()
        bio_item['url'] = str(response.url)
        bio_item['bio'] = bio

        yield bio_item