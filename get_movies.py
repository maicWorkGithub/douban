# coding: utf-8
import requests
from bs4 import BeautifulSoup as BS


# 获得https://movie.douban.com/mine下的
# 电影总数，电影名称、我的评分、标记日期、电影图片、豆瓣链接
# 在MySQL里存一个表格，以供以后node的数据库使用。
# 这个是豆瓣观影报告的jsonp地址https://movie.douban.com/j/standbyme/2015/posters?callback=jsonp_15hrfj5poill4wb
# 生成一个json, 选型：HTML5的filereader接口，或者存储为一个js文件，引入即可。

class GetMovies:
    pass
