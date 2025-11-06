# groupf/tasks/views.py
from django.shortcuts import render

def top_page(request):
    """
    トップページを表示するビュー
    """
    # 将来的にここでデータベースからタスク情報を取得し、context経由でテンプレートに渡します。
    context = {}
    return render(request, 'tasks/index.html', context)

def task_assign(request):
    """
    タスク割り当てページを表示するビュー
    """
    context = {}
    return render(request, 'tasks/task_assign.html', context)

def task_list(request):
    """
    タスク一覧ページを表示するビュー
    """
    context = {}
    return render(request, 'tasks/task_list.html', context)

def task_redister(request):
    """
    タスク登録ページを表示するビュー
    """
    context = {}
    return render(request, 'tasks/task_redister.html', context)
