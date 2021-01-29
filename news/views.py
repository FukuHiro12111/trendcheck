from django.shortcuts import render
from .models import News
import requests
from bs4 import BeautifulSoup


class GetNews(object):
    def get_and_news_information(self):
        # url取得
        load_url = requests.get("https://news.yahoo.co.jp/")
        # webページの解析
        soup = BeautifulSoup(load_url.text, "html.parser")
        # テキスト取得
        hrefs = [elem['href'] for elem in soup.find(
                'div', class_="sc-dYzWWc eYHtfd").find('ul').find_all('a')]
        titles = [elem.text for elem in soup.find(
                'div', class_="sc-dYzWWc eYHtfd").find('ul').find_all('a')]

