# groupf/tasks/urls.py
from django.urls import path
from . import views


urlpatterns = [
    # ルートURL ('/') へのアクセスをviews.top_page関数に紐付ける
    path('', views.top_page, name='top_page'),

    path('task_assign/', views.task_assign, name='task_assign'),
    path('task_board/', views.task_board, name='task_board'),
    path('task_redister/', views.task_redister, name='task_redister'),
    
]