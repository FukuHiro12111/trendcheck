from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.top_url, name='index'),
    path('yahoo/', views.get_news_information, name='yahoo'), # yahooニュース処理
    path('qiita/', views.get_qiita_information, name='qiita'), # yahooニュース処理
]
