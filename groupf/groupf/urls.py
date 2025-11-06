# groupf/groupf/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # ルートURL以下をtasksアプリケーションのurls.pyにルーティングする
    path('', include('tasks.urls')),
]