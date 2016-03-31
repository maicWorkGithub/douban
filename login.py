# coding: utf-8
import json
import time
import requests
import os
from .base_seetings import *
from bs4 import BeautifulSoup as BS
import re



class Client:
    def __init__(self, cookies=None):
        self._session = requests.Session()
        self._session.headers.update(header)
        if cookies is not None:
            assert isinstance(cookies, str)
            self.login_with_cookies(cookies)

    def _get_captcha(self):
        self._session.get(urls['index'])
        html = requests.get(urls['index']).text
        soup = BS(html, "lxml")
        captcha_url = soup.finc('id', "captcha_image")['src']
        pattern = re.compile(r'id=\S+=')
        captcha_id = captcha_url.match(pattern)
        if captcha_url:
            r = self._session.get(captcha_url)
            return r.content, captcha_id

    def login(self, email, password, captcha=None):
        data = {
            'form_email': email,
            'form_password': password,
            # "captcha-solution": "cheese",
            # "captcha-id": "CX4xVgy8fpA45yL18l3jWczX:en",
            'remember': 'on'
        }

        if captcha:
            data['captcha-id'] = captcha['id']

    def login_in_terminal(self):



    def login_with_cookies(self, cookies):
        pass
