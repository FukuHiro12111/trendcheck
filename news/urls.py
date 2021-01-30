from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.top_url, name='index'),
    # ajax処理
    path('yahoo/', views.get_news_information, name='yahoo'),
]
