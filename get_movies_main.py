# coding: utf-8
import json
import re

from bs4 import BeautifulSoup as BS

from base_settings import *
from login import Client

# 获得https://movie.douban.com/mine下的
# 电影总数，电影名称、我的评分、标记日期、电影图片、豆瓣链接
# 在MySQL里存一个表格，以供以后node的数据库使用。
# 这个是豆瓣观影报告的jsonp地址:
#       https://movie.douban.com/j/standbyme/2015/posters?callback=jsonp_15hrfj5poill4wb
# 生成一个json, 选型：HTML5的filereader接口，或者存储为一个js文件，引入即可。

'''
电影栏目下:
我看:main
排行榜:chart
分类: tag
'''


class GetMoviesMain:
    def __init__(self):
        cl = Client()
        self.login = Client.login_with_cookies(cl, 'cookies')
        self._session = cl._session
        self.movie_info = {'movies': []}
        self._get_collect_url(urls['movie'])
        self._get_collect(self.collect_url)

    def _get_collect_url(self, url):
        mine_header = header
        mine_header['Host'] = 'movie.douban.com'
        self._session.headers.update(mine_header)
        html = self._session.get(url + 'mine').text
        html_soup = BS(html, 'lxml')
        # 这里得到的却是https://www.douban.com/mine, 即个人主页.
        # 我修改Host和Referer为movie.douban.com/之后是404
        # 问题原因: 是用了urls里的movie值,这里的地址是https开头的...

        # 第一个是movie.douban.com/mine的解析, 第二个是https://www.douban.com/mine的解析
        person_collect = html_soup.find('div', id='db-movie-mine') or html_soup.find('div', id='movie')

        person_collect_url = person_collect.find('a')
        self.movie_info['total'] = re.findall(r'\d+', person_collect_url.get_text())
        self.collect_url = person_collect_url['href']
        self.user_ID = re.findall(r'\d+', person_collect_url['href'])
        print '您的豆瓣ID为: %s' % self.user_ID[0]

    def _get_collect_page_count(self, url):
        html = self._session.get(url).text
        html_soup = BS(html, 'lxml')
        return html_soup.find('span', class_='thispage')['data-total-page']

    def _get_collect(self, url):
        count = int(self._get_collect_page_count(url))
        step = 15
        data = {
            "sort": "time",
            "rating": "all",
            "filter": "all",
            "mode": "grid"
        }

        for index in range(count):
            data['start'] = step * index
            html = self._session.get(url).text
            html_soup = BS(html, 'lxml')
            items = html_soup.find_all('div', class_='item')
            for item in items:
                self.movie_info['movies'].append({
                    "name": item.find('li', class_='title').find('em').get_text(),
                    'url': item.find('div', class_='pic').find('a')['href'],
                    'image': item.find('div', class_='pic').find('img')['src'],
                    'date': item.find('span', class_='date').get_text(),
                    'score': re.findall(r'\d+', item.find('span', class_='date')
                                        .previous_sibling.previous_sibling['class'][0])[0],

                })

    def create_movies_json(self):
        with open('movies.json', 'w') as f:
            f.write(json.dumps(self.movie_info['movies']))


if __name__ == '__main__':
    gm = GetMoviesMain()
    gm.create_movies_json()
