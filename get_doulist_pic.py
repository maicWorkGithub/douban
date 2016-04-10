# coding: utf-8
from urlparse import urlparse
import time

from bs4 import BeautifulSoup as BS

from login import *

# https://www.douban.com/doulist/14091081/
header = {
    "Host": "www.douban.com",
    "path": "/doulist/14091081",
    "Referer": "https://www.douban.com/people/68749284/doulists/collect",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36"
                  " (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36"
}


class GetDoulistPic:
    def __init__(self):
        self.url = 'https://www.douban.com/doulist/14091081/'
        self.login = Client('cookies')
        self._session = self.login.return_session()
        self._session.headers.update(header)

    def get_first_list(self):
        # 这个直接返回的是一个网页，只能解析网页了
        index_html = self._session.get(self.url).text
        index_html_soup = BS(index_html, 'lxml')
        total_pages = index_html_soup.find('span', class_='thispage')['data-total-page']
        index_doulists = index_html_soup.find_all('div', class_="doulist-item")
        for item in index_doulists:
            yield {
                "title": item.find('div', class_="title").find('a').get_text().strip(),
                "url": item.find('div', class_="title").find('a')['href']
            }

        page, step = 1, 25
        params = {
            "start": 0,
            "sort": "time",
            "sub_type": ""
        }
        while page <= total_pages:
            params['start'] = page * step
            html = self._session.get(self.url, params=params)
            html_soup = BS(html, 'lxml')
            doulists = html_soup.find_all('div', class_="doulist-item")
            for item in doulists:
                yield {
                    "title": item.find('div', class_="title").find('a').get_text().strip(),
                    "url": item.find('div', class_="title").find('a')['href']
                }

            page += 1
            print "first page num: %s, total page: %s" % (page, total_pages)
            time.sleep(0.5)

    def get_small_pic(self):
        small_header = header
        small_header['Referer'] = self.url
        for obj in self.get_first_list():
            small_header['path'] = urlparse(obj['url']).path
            self._session.headers.update(small_header)
            first_html = self._session.get(obj['url'])
            first_html_soup = BS(first_html.text, 'lxml')
            total_pages = first_html_soup.find('span', class_='thispage')['data-total-page']
            for item in first_html_soup.find_all('a', class_="photolst_photo"):
                yield {
                    "title": obj['title'],
                    "pic_url": item['href'],
                    "Parent_url": first_html.url
                }

            step, page = 18, 1
            while page <= total_pages:
                html = self._session.get(obj['url'], params={"start": page * step})
                html_soup = BS(html.text, 'lxml')
                for item in html_soup.find_all('a', class_="photolst_photo"):
                    yield {
                        "title": obj['title'],
                        "pic_url": item['href'],
                        "Parent_url": html.url
                    }
                page += 1
                print "small page num: ", page
                time.sleep(0.5)

    def get_big_pic(self):
        for pic_obj in self.get_small_pic():
            pic_header = header
            pic_header['Referer'] = pic_obj["Parent_url"]
            pic_header['path'] = urlparse(pic_obj['pic_url']).path
            self._session.headers.update(pic_header)
            pic_html = self._session.get(pic_obj['pic_url']).text
            pic_html_soup = BS(pic_html, 'lxml')
            for item in pic_html_soup.find_all('a', class_="mainphoto"):
                yield {
                    "url": item.find('img')['src'],
                    "title": pic_obj['title']
                }

    # 还有一个查看高清大图的，不做了吧，唉...

    def save_pic(self):
        title = ''
        for pic_url in self.get_big_pic():
            count = 1
            if title != pic_url['title']:
                count = 1
            else:
                count += 1

            """
            判断文件类型：
            从网上下载的时候，一般只需要读后缀名称就行了。这里使用的是这个简单的方法
            如果不想读，而且为了安全起见，可以先一股脑保存到本地，然后再用imghdr模块判断后加上
            """
            extension = pic_url['url'][pic_url['url'].rfind('.'):]
            name = pic_url['title'] + ' - ' + str(count) + extension
            s_header = {
                "Host": "img3.doubanio.com",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36"
                              " (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36"
            }
            with open('%s' % name, 'w') as f:
                print name
                self._session.headers.update(s_header)
                pic_content = self._session.get(pic_url['url']).content
                f.write(pic_content)
            title = pic_url['title']

if __name__ == "__main__":
    gdp = GetDoulistPic()
    gdp.save_pic()
