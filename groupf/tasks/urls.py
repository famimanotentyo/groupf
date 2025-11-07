# groupf/tasks/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # ルートURL ('/') へのアクセスをviews.top_page関数に紐付ける
    path('', views.top_page, name='top_page'),

    path('task_assign/', views.task_assign, name='task_assign'),
    path('task_board/', views.task_board, name='task_board'),
    path('task_register/', views.task_register, name='task_register'),
    path('management/', views.management_support_page, name='management_support_page'),
    path('task-assign/', views.task_assign_page, name='task_assign_page'),
    path('task-board/', views.task_board_page, name='task_board_page'),
    path('task-register/', views.task_register_page, name='task_register_page'),
    path('task-guide/', views.task_guide_page, name='task_guide_page'),
    path('account/create/', views.create_account, name='create_account'),
    path('account/create/success/', views.account_create_success, name='account_create_success'),
    path('account/', views.account_management_page, name='account_management_page'),
    
]