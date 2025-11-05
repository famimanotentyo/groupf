# tasks/views.py
from django.shortcuts import render

def task_board(request):
    """
    タスクボード画面（画面設計タスクボード.jpg）を表示
    """
    # いまは空のHTMLを返すだけ
    return render(request, 'tasks/task_board.html')

def task_register(request):
    """
    タスク登録画面（画面設計タスク登録.jpg）を表示
    """
    return render(request, 'tasks/task_register.html')

def task_assign(request):
    """
    タスク割り当て画面（画面設計タスク割り当て.jpg）を表示
    """
    return render(request, 'tasks/task_assign.html')

def jyousitop(request):
    """
    上司トップ画面を表示
    """
    return render(request, 'tasks/jyousitop.html')  