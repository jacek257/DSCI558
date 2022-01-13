# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 14:18:56 2021

@author: Jimi
"""

from bs4 import BeautifulSoup as soup
from datetime import datetime
import uuid

import scrapy
from cast.items import CastItem

class CastSpider(scrapy.Spider):
    name = "cast"
    
    allowed_domains = ['metacritic.com']
    # 100 for test, 5000 for submission
    # 30 people per page
    # 100/30 = 3.33 ~ 3
    # 5000/30 = 166.6 ~ 167
    start_urls = ['https://www.metacritic.com/browse/movies/people/popular?page={}'.format(idx) for idx in range(0, 167)]
    
    def parse(self, response):
    
        cast_soup = soup(response.body, 'html.parser')
        
        for person in cast_soup.find_all('div', class_='title'):
            cast_link = "https://www.metacritic.com" + person.select('a')[0]['href']
            yield scrapy.Request(cast_link, callback=self.parse_cast)
            
    def parse_cast(self, response):
        cast_item = CastItem()
        
        # static stuff
        cast_item['id'] = uuid.uuid4().hex.upper()
        cast_item['url'] = str(response.url)
        cast_item['timestamp_crawl'] = datetime.now()
        
        # make soup
        cast_soup = soup(response.body, 'html.parser')
        
        # isolate main section
        main = cast_soup.find('div', id='main')
        
        # get name
        name = main.find('h1', class_='person_title').text
        cast_item['name'] = str(name).strip()
        
        # get upto 5 most recent movies
        ls = []
        try:
            movies = main.find('table', class_='credits person_credits')
            try:
                movie_list = movies.find('tbody').find_all('tr')
                count = 0
                for movie in movie_list:
                    count += 1
                    if count > 5:
                        break
                    
                    name = ""
                    year = -1
                    role = ""
                    
                    try:
                        name = movie.find('a').text.strip()
                    except:
                        pass
                    
                    try:
                        year = int(movie.find('td', class_='year').text.strip().split(' ')[-1])
                    except:
                        pass
                    
                    try:
                        role = movie.find('td', class_='role').text.strip()
                    except:
                        pass
                    
                    ls.append({'title':name, "year":year, "role":role})
            except:
                pass
        except:
            pass
        cast_item['movies'] = ls
        
        yield cast_item
                
