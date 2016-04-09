# coding: utf-8
import json
import requests
import urllib
from login import Client
import time


# 拉取豆瓣高分没看过的，评分大于sore分数的电影。一共收集x部电影
class GetMovieExplore:
    def __init__(self):
        self.login = Client('cookies')
        self.sore = 8
        self.x = 1000
        self._session = self.login.session()
        self.header = {
            'Referer': 'https://movie.douban.com/explore',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0',
            'Host': 'movie.douban.com',
            'x-requested-with': "XMLHttpRequest"
        }
        self._session.headers.update(self.header)

    def get_explore_json(self):
        result = []
        data = {
            "type": "movie",
            "tag": "豆瓣高分",
            "sort": "recommend",
            "watched": "on",
            "page_limit": 20,
            "page_start": 0
        }
        count = 0
        while len(result) < self.x:
            last_len = len(result)
            data['page_start'] = data['page_limit'] * count
            url_str = '/j/search_subjects?'
            for key in data:
                url_str += key + '=' + urllib.quote(str(data[key]))
            count += 1
            self.header['path'] = url_str
            req = requests.Request('GET',
                                   'http://movie.douban.com/j/search_subjects',
                                   params=data,
                                   headers=self.header)
            prepped = self._session.prepare_request(req)
            resp = self._session.send(prepped)
            result.extend(resp.json()['subjects'])
            time.sleep(2)
            if last_len == len(result):
                break

        # todo: sort
        # result = sorted(result.iteritems(), key=lambda d:d[1], reverse = True)
        with open('high_mark_movie.json', 'w') as f:
            f.write(json.dumps(result))
if __name__ == "__main__":
    gme = GetMovieExplore()
    gme.get_explore_json()
