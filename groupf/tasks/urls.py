# groupf/tasks/urls.py
from django.urls import path
from . import views

#aaa
urlpatterns = [
    # ルートURL ('/') へのアクセスをviews.top_page関数に紐付ける
    path('', views.top_page, name='top_page'),

    path('task_assign/', views.task_assign, name='task_assign'),
    path('task_board/', views.task_board, name='task_board'),
    path('task_register/', views.task_register, name='task_register'),
    path('management/', views.management_support_page, name='management_support_page')
    
]