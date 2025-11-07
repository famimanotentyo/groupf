# groupf/tasks/views.py
from django.shortcuts import render, redirect

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
def task_assign_page(request):
    context = {
        'page_title': 'タスク割り当て'
    }
    return render(request, 'tasks/task_assign.html', context)
def task_board_page(request):
    context = {
        'page_title': 'タスクボード'
    }
    return render(request, 'tasks/task_board.html', context)
def task_register_page(request):
    context = {
        'page_title': 'タスク登録'
    }
    return render(request, 'tasks/task_register.html', context)
def task_guide_page(request):
    context = {
        'page_title': 'タスクガイド'
    }
    return render(request, 'tasks/task_guide.html', context)

def create_account(request):
    """
    アカウント作成フォームの表示と処理
    """
    if request.method == 'POST':

        # ここでは一旦、成功ページにリダイレクトします。
        return redirect('tasks:account_create_success')
    
    return render(request, 'tasks/account_create.html')

def account_create_success(request):
    """
    アカウント作成成功画面の表示
    """
    return render(request, 'tasks/account_create_success.html')
def account_management_page(request):
    context = {
        'page_title': 'アカウント管理'
    }
    return render(request, 'tasks/account_management.html', context)
