# coding: utf-8

import requests
import os
import json

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
    "page_limit": "20",
    "page_start": 40
}

headers = {
    'Referer': 'https://www.douban.com',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0',
    'Host': 'movie.douban.com',
    'x-requested-with': "XMLHttpRequest",
    "path": "/j/search_subjects?type=movie&tag=%E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&sort=recommend&watched=on&page_limit=20&page_start=40"
}
req = requests.Request('GET', 'http://movie.douban.com/explore', params=data, headers=headers)

prepped = s.prepare_request(req)

# do something with prepped.body
# do something with prepped.headers

resp = s.send(prepped)

print(resp.status_code)
