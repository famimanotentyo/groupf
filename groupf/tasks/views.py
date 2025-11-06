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

def task_board(request):
    """
    タスク一覧ページを表示するビュー
    """
    context = {}
    return render(request, 'tasks/task_board.html', context)

def task_register(request):
    """
    タスク登録ページを表示するビュー
    """
    context = {}
    return render(request, 'tasks/task_register.html', context)
def management_support_page(request):
    """
    マネジメント支援ページを表示するビュー
    """
    # ★★★ こちらにも、ヘッダー用のタイトルを渡します ★★★
    context = {
        'page_title': 'マネジメント支援'
    }
    return render(request, 'tasks/management_support.html', context)
