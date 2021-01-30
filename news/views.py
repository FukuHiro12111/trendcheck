from django.http import HttpResponse
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .models import News
from django.views.generic import ListView


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

    content = {'list': zip(titles, urls),}

    return HttpResponse(content)
    

# class GetNewsView(object):
#     template_name = "news/news_list.html"

    

# class NewsList(ListView):
#     template_name = 'news/news_list.html'
#     model = News
    # return render(request,template_name)
