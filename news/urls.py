from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.NewsList.as_view(), name='news'),
]
