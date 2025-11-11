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
    path('account/create/', views.account_create_page, name='account_create_page'),
    path('account/create/success/', views.account_create_success_page, name='account_create_success_page'),
    path('account/', views.account_management_page, name='account_management_page'),
    path('accounts/', views.account_list_page, name='account_list_page'),
    path('myaccount/', views.account_detail_page, name='account_detail_page'),
    path('logout/', views.account_logout_view_page, name='account_logout_view_page'),
    path('logout/success/', views.account_logout_success_page, name='logout_success'),
    path('login/', views.account_login_view_page, name='account_login_view_page'), # 仮のログインURL
]