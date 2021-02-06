from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.views.generic import ListView
from news.models import News
from .forms import MylistNews

def top_url(request):
    '''トップページ'''
    return render(request, 'news/scraping_list.html')


def get_news_information(request):
    '''Yahooニューススクレイピング'''
    # url取得
    load_url = requests.get("https://news.yahoo.co.jp/")
    # webページの解析
    soup = BeautifulSoup(load_url.text, "html.parser")
    # テキスト取得
    urls = [elem['href'] for elem in soup.find(
            'div', class_="sc-fFTYTi KSKOO").find('ul').find_all('a')]
    titles = [elem.text for elem in soup.find(
            'div', class_="sc-fFTYTi KSKOO").find('ul').find_all('a')]

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


def create(request):
    '''Mylistの作成'''
    if request.method == "POST":
        form = MylistNews(request.POST)
        if form.is_valid():
            create_mylist = News(title=request.POST['title'],
                                                link=request.POST['link'])
            create_mylist.save()
            # status=204 is not return
            return HttpResponse(status=204)           
        else:
            return HttpResponse(status=400)


class MyListView(ListView):
    model = News
    ordering = ['-created_on']
