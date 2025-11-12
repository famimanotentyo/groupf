# groupf/tasks/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import logout # logout関数をインポート


def top_page(request):
    """
    トップページを表示するビュー
    """
    # 将来的にここでデータベースからタスク情報を取得し、context経由でテンプレートに渡します。
    context = {}
    return render(request, 'index.html', context)

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

def account_create_page(request):
    """
    アカウント作成フォームの表示と処理
    """
    if request.method == 'POST':

        # ここでは一旦、成功ページにリダイレクトします。
        return redirect('tasks:account_create_success')
    
    return render(request, 'accounts/account_create.html')

def account_create_success_page(request):
    """
    アカウント作成成功画面の表示
    """
    return render(request, 'accounts/account_create_success.html')
def account_management_page(request):
    context = {
        'page_title': 'アカウント管理'
    }
    return render(request, 'accounts/account_management.html', context)

def account_list_page(request):
    """
    アカウント閲覧画面を表示
    """
    # 将来的にはここで
    # users = User.objects.all() のようにデータを取得し、
    # context = {'users': users} としてテンプレートに渡します。
    
    return render(request, 'accounts/account_list.html')

def account_detail_page(request):
    """
    ログイン中のユーザー自身のアカウント詳細画面を表示
    """
    # 将来的には request.user からユーザー情報を取得してテンプレートに渡します
    # context = {'user': request.user}
    return render(request, 'accounts/account_detail.html')

def account_logout_view_page(request):
    """
    ユーザーをログアウトさせ、ログアウト成功画面にリダイレクト
    """
    #logout(request) # Django標準のログアウト処理
    return redirect('logout_success') # ログアウト成功画面へリダイレクト　ここ適当

def account_logout_success_page(request):
    """
    ログアウト成功画面を表示
    """
    return render(request, 'accounts/account_logout_success.html')

# ログイン画面のビュー (仮)
def account_login_view_page(request):
    """
    ログイン画面を表示 (実際にはdjango.contrib.auth.views.LoginViewなどを使用)
    """
    return render(request, 'accounts/login.html') # login.htmlは別途作成が必要です
def manual_list(request):
    # 今後、ここでデータベースからマニュアル一覧を取得する処理などを書きます
    context = {} 
    return render(request, 'manual/manual_list.html', context)
def interview_request_page(request):
    context = {
        'page_title': '面談依頼'
    }
    return render(request, 'tasks/interview_request.html', context)