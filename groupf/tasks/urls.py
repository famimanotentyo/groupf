# tasks/urls.py (新規作成)
from django.urls import path
from . import views

# この 'app_name' があると、HTML側でURLを呼び出しやすくなります
app_name = 'tasks'

urlpatterns = [
    # 例: http://.../ でタスクボード画面を表示
    path('', views.task_board, name='task_board'),
    
    # 例: http://.../new/ でタスク登録画面を表示
    path('new/', views.task_register, name='task_register'),
    
    # 例: http://.../assign/ でタスク割り当て画面を表示
    path('assign/', views.task_assign, name='task_assign'),
]