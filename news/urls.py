from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.top_url, name='index'),
    path('yahoo/', views.get_news_information, name='yahoo'),  # yahooニュース
    path('qiita/', views.get_qiita_information, name='qiita'),  # qiitaトレンド
    # path('create_mylist/', views.post_mylist, name='post_mylist'),  # mylist保存
]
