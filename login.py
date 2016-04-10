# coding: utf-8
import json
import requests
import os
from base_settings import *
from bs4 import BeautifulSoup as BS
import re


class Client:
    def __init__(self, cookies=None):
        self._session = requests.Session()
        self._session.headers.update(header)
        self.login_succeed = True
        if cookies is not None:
            assert isinstance(cookies, str)
            if os.path.isfile(cookies):
                self.login_with_cookies(cookies)
            else:
                self.create_cookies()

    def _get_captcha(self):
        html = self._session.get(urls['index']).text
        soup = BS(html, "lxml")
        find_captcha = soup.find(id="captcha_image")
        if find_captcha:
            captcha_url = find_captcha['src']
            pattern = re.compile(r'id=\S+&')
            captcha_id = re.findall(pattern, captcha_url)[0][3:-1]
            r = self._session.get(captcha_url)
            return r.content, captcha_id
        else:
            self.has_captcha = False

    def login(self, email, password, captcha=None):
        data = {
            'form_email': email,
            'form_password': password,
            'remember': 'on',
            'source': 'index_nav'  # 不知道这个是不是必须的
        }

        if captcha:
            data['captcha-id'] = captcha['id']
            data['captcha-solution'] = captcha['word']

        r = self._session.post(urls['index'] + '/accounts/login', data=data)
        # 这里是检测有没有登录成功（污啊）。因为豆瓣不管登录成功与否，都会返回一个网页，没有任何状态值。只能通过网页关键字匹配。
        html = BS(r.text, 'lxml')
        # 找到 li.nav-user-account>a>span[0].text, 这个里面有XXX的账号三个字，就匹配这三个字好了，然后还能再给点交互
        account_li = html.find('li', class_="nav-user-account")
        if account_li:
            self.login_succeed = True
            username = account_li.find('span').get_text()[:-3]
            cookies_str = json.dumps(self._session.cookies.get_dict()) or ""
            return username,  cookies_str
        else:
            self.login_succeed = False

    def login_in_terminal(self):
        print '====== douban login ====='

        email = raw_input('email: ')
        password = raw_input('password: ')
        print 'email: %s, password: %s' % (email, password)
        captcha = None

        # ( captcha_url, captcha_id )
        captcha_tuple = self._get_captcha()
        if captcha_tuple:
            captcha = {
                'url': captcha_tuple[0],
                'id': captcha_tuple[1]
            }

            with open('captcha.gif', 'wb') as f:
                f.write(captcha_tuple[0])

            print('please check captcha.gif for captcha')
            captcha['word'] = raw_input('captcha: ')
            os.remove('captcha.gif')

        print '====== logging.... ====='
        if self.login_succeed:
            username, cookies = self.login(email, password, captcha)
            print 'Welcome, %s , You login successfully!' % username
            return cookies
        else:
            print 'Oops, login failed.'

    def create_cookies(self):
        cookies_str = self.login_in_terminal()
        if cookies_str:
            with open('cookies', 'w') as f:
                f.write(cookies_str)
            print 'cookies file created.'
        else:
            print 'can\'t create cookies.'

    def login_with_cookies(self, cookies):
        if os.path.isfile(cookies):
            with open(cookies) as f:
                cookies = f.read()
        cookies_dict = json.loads(cookies)
        self._session.cookies.update(cookies_dict)

    def return_session(self):
        assert self.login_succeed
        return self._session


if __name__ == '__main__':
    lg = Client()
    lg.create_cookies()
