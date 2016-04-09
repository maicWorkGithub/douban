# -*- coding: UTF-8 -*-
import codecs
import json

arr = '{"subjects":[{"rate":"8.3","cover_x":2100,"is_beetle_subject":false,"title":"希特勒回来了","url":"https:\/\/movie.douban.com\/subject\/26585014\/","playable":false,"cover":"https://img1.doubanio.com\/view\/movie_poster_cover\/lpst\/public\/p2329535697.jpg","id":"26585014","cover_y":3000,"is_new":true},{"rate":"8.6","cover_x":600,"is_beetle_subject":false,"title":"阿赫迈德王子历险记","url":"https:\/\/movie.douban.com\/subject\/1302814\/","playable":true,"cover":"https://img3.doubanio.com\/view\/movie_poster_cover\/lpst\/public\/p456760460.jpg","id":"1302814","cover_y":800,"is_new":true},{"rate":"8.4","cover_x":1105,"is_beetle_subject":false,"title":"我杀了我妈妈","url":"https:\/\/movie.douban.com\/subject\/3707070\/","playable":true,"cover":"https://img3.doubanio.com\/view\/movie_poster_cover\/lpst\/public\/p490697335.jpg","id":"3707070","cover_y":1500,"is_new":true},{"rate":"8.8","cover_x":2025,"is_beetle_subject":false,"title":"房间","url":"https:\/\/movie.douban.com\/subject\/25724855\/","playable":false,"cover":"https://img3.doubanio.com\/view\/movie_poster_cover\/lpst\/public\/p2259715855.jpg","id":"25724855","cover_y":3000,"is_new":false},{"rate":"8.3","cover_x":8265,"is_beetle_subject":false,"title":"卡罗尔","url":"https:\/\/movie.douban.com\/subject\/10757577\/","playable":false,"cover":"https://img3.doubanio.com\/view\/movie_poster_cover\/lpst\/public\/p2312679154.jpg","id":"10757577","cover_y":11780,"is_new":false},{"rate":"8.8","cover_x":1893,"is_beetle_subject":false,"title":"聚焦","url":"https:\/\/movie.douban.com\/subject\/25954475\/","playable":false,"cover":"https://img1.doubanio.com\/view\/movie_poster_cover\/lpst\/public\/p2263822658.jpg","id":"25954475","cover_y":2800,"is_new":false},{"rate":"8.1","cover_x":1000,"is_beetle_subject":false,"title":"师父","url":"https:\/\/movie.douban.com\/subject\/25919910\/","playable":true,"cover":"https://img1.doubanio.com\/view\/movie_poster_cover\/lpst\/public\/p2293405567.jpg","id":"25919910","cover_y":1400,"is_new":false},{"rate":"8.6","cover_x":600,"is_beetle_subject":false,"title":"心迷宫","url":"https:\/\/movie.douban.com\/subject\/25917973\/","playable":true,"cover":"https://img3.doubanio.com\/view\/movie_poster_cover\/lpst\/public\/p2275298525.jpg","id":"25917973","cover_y":851,"is_new":false},{"rate":"8.0","cover_x":4050,"is_beetle_subject":false,"title":"丹麦女孩","url":"https:\/\/movie.douban.com\/subject\/3071604\/","playable":false,"cover":"https://img3.doubanio.com\/view\/movie_poster_cover\/lpst\/public\/p2264778990.jpg","id":"3071604","cover_y":6000,"is_new":false},{"rate":"8.6","cover_x":1772,"is_beetle_subject":false,"title":"模仿游戏","url":"https:\/\/movie.douban.com\/subject\/10463953\/","playable":false,"cover":"https://img3.doubanio.com\/view\/movie_poster_cover\/lpst\/public\/p2255040492.jpg","id":"10463953","cover_y":2480,"is_new":false},{"rate":"8.6","cover_x":904,"is_beetle_subject":false,"title":"海街日记","url":"https:\/\/movie.douban.com\/subject\/25895901\/","playable":false,"cover":"https://img1.doubanio.com\/view\/movie_poster_cover\/lpst\/public\/p2232247487.jpg","id":"25895901","cover_y":1280,"is_new":false},{"rate":"8.5","cover_x":787,"is_beetle_subject":false,"title":"再次出发之纽约遇见你","url":"https:\/\/movie.douban.com\/subject\/6874403\/","playable":true,"cover":"https://img3.doubanio.com\/view\/movie_poster_cover\/lpst\/public\/p2250287733.jpg","id":"6874403","cover_y":1153,"is_new":false},{"rate":"8.3","cover_x":1280,"is_beetle_subject":false,"title":"初恋这件小事","url":"https:\/\/movie.douban.com\/subject\/4739952\/","playable":true,"cover":"https://img3.doubanio.com\/view\/movie_poster_cover\/lpst\/public\/p1505312273.jpg","id":"4739952","cover_y":1829,"is_new":false},{"rate":"9.1","cover_x":2000,"is_beetle_subject":false,"title":"辩护人","url":"https:\/\/movie.douban.com\/subject\/21937445\/","playable":true,"cover":"https://img3.doubanio.com\/view\/movie_poster_cover\/lpst\/public\/p2158166535.jpg","id":"21937445","cover_y":2865,"is_new":false},{"rate":"8.7","cover_x":2126,"is_beetle_subject":false,"title":"荒蛮故事","url":"https:\/\/movie.douban.com\/subject\/24750126\/","playable":true,"cover":"https://img3.doubanio.com\/view\/movie_poster_cover\/lpst\/public\/p2192834364.jpg","id":"24750126","cover_y":3000,"is_new":false},{"rate":"8.9","cover_x":550,"is_beetle_subject":false,"title":"被嫌弃的松子的一生","url":"https:\/\/movie.douban.com\/subject\/1787291\/","playable":false,"cover":"https://img1.doubanio.com\/view\/movie_poster_cover\/lpst\/public\/p453723669.jpg","id":"1787291","cover_y":775,"is_new":false},{"rate":"8.7","cover_x":1000,"is_beetle_subject":false,"title":"恐怖直播","url":"https:\/\/movie.douban.com\/subject\/21360417\/","playable":true,"cover":"https://img3.doubanio.com\/view\/movie_poster_cover\/lpst\/public\/p2016930906.jpg","id":"21360417","cover_y":1433,"is_new":false},{"rate":"8.7","cover_x":514,"is_beetle_subject":false,"title":"低俗小说","url":"https:\/\/movie.douban.com\/subject\/1291832\/","playable":true,"cover":"https://img3.doubanio.com\/view\/movie_poster_cover\/lpst\/public\/p1910902213.jpg","id":"1291832","cover_y":755,"is_new":false},{"rate":"8.0","cover_x":1408,"is_beetle_subject":false,"title":"暗杀","url":"https:\/\/movie.douban.com\/subject\/25823132\/","playable":true,"cover":"https://img3.doubanio.com\/view\/movie_poster_cover\/lpst\/public\/p2265025290.jpg","id":"25823132","cover_y":2009,"is_new":false},{"rate":"8.6","cover_x":3375,"is_beetle_subject":false,"title":"时空恋旅人","url":"https:\/\/movie.douban.com\/subject\/10577869\/","playable":true,"cover":"https://img3.doubanio.com\/view\/movie_poster_cover\/lpst\/public\/p2070153774.jpg","id":"10577869","cover_y":5000,"is_new":false}]}'

# print json.loads(arr)['subjects']
# f = codecs.open('kk.json', 'wb', encoding='utf-8')
# f.write(json.dumps(json.loads(arr)['subjects']))

print (json.dumps(json.loads(arr)['subjects']))
