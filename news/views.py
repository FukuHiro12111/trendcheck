from django.http import JsonResponse
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.views.generic import ListView
from .models import News
from .forms import NewsCreateForm


def top_url(request):
    '''トップページ'''
    return render(request, 'news/news_list.html')

def get_news_information(request):
    '''Yahooニューススクレイピング'''
    # url取得
    load_url = requests.get("https://news.yahoo.co.jp/")
    # webページの解析
    soup = BeautifulSoup(load_url.text, "html.parser")
    # テキスト取得
    urls = [elem['href'] for elem in soup.find(
            'div', class_="sc-dYzWWc eYHtfd").find('ul').find_all('a')]
    titles = [elem.text for elem in soup.find(
            'div', class_="sc-dYzWWc eYHtfd").find('ul').find_all('a')]

    # zip関数をlistにキャスト
    content = {'list': list(zip(titles, urls)),}

    return JsonResponse(content)

def get_qiita_information(request):
    '''Qiitaトレンドスクレイピング'''
    #  # url取得
    load_url = requests.get("https://qiita.com/")
    # webページの解析
    soup = BeautifulSoup(load_url.text, "html.parser")

    elems = soup.find_all('article', class_="css-81mxb5")

    titles = []
    urls = []
    for elem in elems:
        # テキスト取得
        for es in elem.find_all('h2'):
            for e in es.find_all('a'):
                titles.append(e.text)
                urls.append(e['href'])

    # zip関数をlistにキャスト
    content = {'list': list(zip(titles, urls)),}

    return JsonResponse(content)

# class NewsList(ListView):
#     template_name = 'news/news_list.html'
#     model = News
#     return render(request,template_name)
