# coding: utf-8
import json
import requests
from requests import Request
from bs4 import BeautifulSoup as BS
from base_settings import *
from login import Client


class RequestWithSharp(requests.Session):
    def prepare_request(self, data):
        p = super(RequestWithSharp, self).prepare_request(data)
        p.url = p.url.replace('?', '#!')
        return p


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

    def get_explore_json(self):
        data = {
            "type": "movie",
            "tag": "豆瓣高分",
            "sort": "recommend",
            "watched": "on",
            "page_limit": 20,
            "page_start": 0
        }
        page_count = 0
        # html = self._session.get(self.url, params=data, headers=header)
        req = Request('GET',
                      urls['movie'] + 'j/search_subjects',
                      data=data,
                      headers=header)
        sharp = RequestWithSharp()
        req = sharp.prepare_request(req)
        html = self._session.send(req)
        while len(self.high_mark_movies) < self.x:

            page_count += 1
            data["page_start"] = data['page_limit'] * page_count

if __name__ == "__main__":
    gme = GetMovieExplore()
    gme.get_explore_json()

# https://movie.douban.com/explore?sort=recommend&page_limit=20&tag=%E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&watched=on&page_start=0&type=movie
# https://movie.douban.com/explore#!type=movie&tag=%E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&sort=recommend&watched=on&page_limit=20&page_start=0