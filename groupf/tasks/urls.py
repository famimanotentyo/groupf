# groupf/tasks/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # ルートURL ('/') へのアクセスをviews.top_page関数に紐付ける
    path('', views.top_page, name='top_page'),
]