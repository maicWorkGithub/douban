# coding: utf-8
import json
import requests
from bs4 import BeautifulSoup as BS
from base_settings import *
from login import Client
from requests import PreparedRequest


# 拉取豆瓣高分没看过的，评分大于sore分数的电影。一共收集x部电影
class GetMovieExplore:
    def __init__(self):
        self.login = Client('cookies')
        self.sore = 8
        self.x = 20
        self._session = self.login.session()
        self.url = urls['movie'] + "explore"
        explore_header = header
        explore_header['Host'] = 'movie.douban.com'
        explore_header['Referer'] = "https://movie.douban.com/explore"
        explore_header['x-requested-with'] = "XMLHttpRequest"
        # path: /j/search_subjects?type=movie&tag=%E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&sort=recommend&watched=on&page_limit=20&page_start=0
        self._session.headers.update(explore_header)
        self.high_mark_movies = []

    def get_ecplore_page(self):
        data = {
            "type": "movie",
            "tag": "豆瓣高分",
            "sort": "recommend",
            "watched": "on",
            "page_limit": "20",
            "page_start": 0
        }
        html = self._session.get(self.url, params=data, headers=header)
        # todo: 考虑给get增加一个关键字，默认为问号，其他可以自己指定
        print html.json
        # while len(self.high_mark_movies) < self.x:
        #
        #
        #     data["page_start"] += 1

if __name__ == "__main__":
    gme = GetMovieExplore()
    gme.get_ecplore_page()

# https://movie.douban.com/explore?sort=recommend&page_limit=20&tag=%E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&watched=on&page_start=0&type=movie
# https://movie.douban.com/explore#!type=movie&tag=%E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&sort=recommend&watched=on&page_limit=20&page_start=0