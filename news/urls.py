from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'news'
urlpatterns = [
    path('', views.top_url, name='index'),
    path('yahoo/', views.get_news_information, name='yahoo'),  # yahooニュース
    path('qiita/', views.get_qiita_information, name='qiita'),  # qiitaトレンド
    path('create/', views.create, name='create'),  # mylist保存
    path('mylist/', views.MyListView.as_view(), name='mylist'),  # mylist一覧
]
