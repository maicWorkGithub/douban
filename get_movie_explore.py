# coding: utf-8
import json
import requests
from bs4 import BeautifulSoup as BS
from base_settings import *
from login import Client


# 拉取豆瓣高分没看过的，评分大于sore分数的电影。一次x部电影
class GetMovieExplore:
    def __init__(self):
        self.login = Client()
        self.sore = 8
        self.x = 30
        self._session = self.login.session()
        self.url = urls['explore']
        explore_header = header
        explore_header['Host'] = 'movie.douban.com'
        explore_header['Referer'] = "https://movie.douban.com/explore"
        explore_header['x-requested-with'] = "XMLHttpRequest"
        # path: /j/search_subjects?type=movie&tag=%E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&sort=recommend&watched=on&page_limit=20&page_start=0
        self._session.headers.update(explore_header)

    def get_ecplore_page(self):
        data = {
            "type": "movie",
            "tag": "豆瓣高分",
            "sort": "recommend",
            "watched": "on",
            "page_limit": "20",
            "page_start": "0"
        }

        html = self._session.get(self.url, params=data, header=header).text
        html_soup = BS(html, 'lxml')

