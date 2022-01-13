# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 14:46:28 2021

@author: Jimi
"""

from bs4 import BeautifulSoup as soup
from datetime import datetime
import uuid

import scrapy
from movie.items import MovieItem

class MovieSpider(scrapy.Spider):
    name = "movie"
    
    allowed_domains = ['imdb.com']
    # 100 for test, 5000 for submission
    start_urls = ['https://www.imdb.com/search/title/?title_type=feature&genres=comedy&start={}'.format(idx) for idx in range(1, 5000, 50)]

            
    def parse(self, response):
    
        page_soup = soup(response.body, 'html.parser')
        
        for item in page_soup.select(".lister-item-header"):
            movie_link = "https://www.imdb.com" + item.select('a')[0]['href']
            yield scrapy.Request(movie_link, callback=self.parse_movie)
    
    def parse_movie(self, response):
        movie_item = MovieItem()
        
        # static stuff
        movie_item['id'] = uuid.uuid4().hex.upper()
        movie_item['url'] = str(response.url)
        movie_item['timestamp_crawl'] = datetime.now()
        
        # make soup
        movie_soup = soup(response.body, 'html.parser')
        
        # title detail div
        details = movie_soup.find('div', id='title-overview-widget')
        
        # get title
        title = details.h1.text
        title = ' '.join(title.split('\xa0')[:-1])
        movie_item['title'] = title
        
        # get Directors and Casts
        infos = details.find_all('div', class_='credit_summary_item')
        for info in infos:
            if info.h4.text == 'Writers:':
                continue
            elif info.h4.text == 'Directors:':
                people = info.find_all('a')
                if 'See full' in people[-1].text:
                    people = people[:-1]
                movie_item['director'] = [person.text for person in people]
            elif info.h4.text == 'Stars:':
                people = info.find_all('a')
                if 'See full' in people[-1].text:
                    people = people[:-1]
                movie_item['cast'] = [person.text for person in people]
                
        # get geners
        storyline = movie_soup.find_all('div', class_='see-more inline canwrap')
        for thing in storyline:
            if thing.h4.text == 'Genres:':
                genres = thing.find_all('a')
                movie_item['genres'] = [genre.text.strip() for genre in genres]
        
                
        # get release date
        try:
            subtext = details.find('div', class_='subtext')
            release_date = subtext.find(title='See more release dates').text
            split = release_date.split(' ')
            if len(split) > 3:
                release_date = ' '.join(split[:3])
        except:
            release_date = ''
        movie_item['release_date'] = release_date
        
        yield movie_item