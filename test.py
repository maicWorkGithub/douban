# coding: utf-8

import requests
import os
import json
# import urlparse
import urllib
import codecs
# import urllib2


s = requests.Session()
if os.path.isfile('cookies'):
    with open('cookies') as f:
        cookies = f.read()
cookies_dict = json.loads(cookies)

s.cookies.update(cookies_dict)

data = {
    "type": "movie",
    "tag": "豆瓣高分",
    "sort": "recommend",
    "watched": "on",
    "page_limit": 20,
    "page_start": 0
}
movie_json = []
headers = {
    'Referer': 'https://movie.douban.com/explore',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0',
    'Host': 'movie.douban.com',
    'x-requested-with': "XMLHttpRequest",
    "path": "/j/search_subjects?type=movie&tag=%E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&"
            "sort=recommend&watched=on&page_limit=20&page_start=20"
}
# urlparse.urlparse()
# print urllib.quote('http://movie.douban.com/explore/豆瓣热门')
count = 0
while len(movie_json) < 80:
    data['page_start'] = data['page_limit'] * count
    url_str = '/j/search_subjects?'
    for key in data:
        url_str += key + '=' + urllib.quote(str(data[key]))
    count += 1
    headers['path'] = url_str
    req = requests.Request('GET',
                           'http://movie.douban.com/j/search_subjects',
                           params=data,
                           headers=headers)
    prepped = s.prepare_request(req)
    resp = s.send(prepped)
    movie_json.extend(resp.json()['subjects'])

# with codecs.open('we.json', 'w', encoding='utf-8') as f:
#     f.write(json.dumps(movie_json))

f = codecs.open('we.json', 'wb', encoding='UTF-8')
f.write(json.dumps(movie_json).decode('utf-8'))



