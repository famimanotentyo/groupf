# groupf/tasks/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import logout # logout関数をインポート
from django.contrib import messages # メッセージフレームワークをインポート
from django.conf import settings # settings.pyからAPIキーを読み込む
import google.generativeai as genai # Gemini SDKをインポート

from .forms import TaskRegisterForm # 作成したフォームをインポート
from .models import Task, Tag # TaskとTagモデルをインポート
from datetime import datetime # 日付/時刻の操作に必要 (必要に応じて)


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
#def task_register_page(request):
#    context = {
#        'page_title': 'タスク登録'
#    }
#    return render(request, 'tasks/task_register.html', context)
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
    return render(request, 'manual/interview_request.html', context)
def interview_advice_menu_page(request):
    context = {
        'page_title': '面談アドバイス'
    }
    return render(request, 'tasks/interview_advice_menu.html', context)


# --- ここからタスク登録関連 ---

# Gemini API の設定 (settings.py からキーを読み込む)
genai.configure(api_key=settings.GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-pro') # Gemini Pro モデルを使用

# タグ生成プロンプトの定義
TAG_GENERATION_PROMPT_TEMPLATE = """
以下のタスク名から、ハッシュタグ形式で20個以内の関連タグを生成してください。
タグには必ず #難易度 (高、中、低) のいずれか一つを含めてください。

例: 議事録の製作
出力: #議事録 #文章作成 #ドキュメント作成 #ビジネス文書 #情報整理 #効率化 #会議 #記録 #難易度中

タスク名: {task_title}
出力:
"""

def generate_tags_with_gemini(task_title):
    """
    Gemini APIを使用してタスク名からタグを生成する
    """
    try:
        prompt = TAG_GENERATION_PROMPT_TEMPLATE.format(task_title=task_title)
        response = model.generate_content(prompt)
        # 応答からテキストを抽出し、ハッシュタグ部分のみを整形
        generated_text = response.text.strip()
        
        # タグの整形 (ハッシュタグとスペースで区切り、重複を削除)
        # まず、応答テキストからタグ部分を抽出し、#で分割
        raw_tags = [tag.strip() for tag in generated_text.split('#') if tag.strip()]
        
        # 各タグの先頭に#を付け直し、重複を削除し、最大20個に制限
        processed_tags = []
        for tag in raw_tags:
            if not tag.startswith('#'):
                tag = '#' + tag
            if tag not in processed_tags:
                processed_tags.append(tag)
            if len(processed_tags) >= 20: # 最大20個
                break
        
        return " ".join(processed_tags) # スペース区切りで返す
        
    except Exception as e:
        print(f"Gemini API呼び出しエラー: {e}")
        # エラー時はデフォルトタグを返すか、エラーとして処理
        return "#エラー #タグ生成失敗 #難易度不明" # エラー時のフォールバック

def task_register_page(request):
    """
    タスク登録ページを表示・処理するビュー
    """
    if request.method == 'POST':
        form = TaskRegisterForm(request.POST)
        if form.is_valid():
            # フォームデータを保存するが、commit=FalseでDBにはまだ保存しない
            task = form.save(commit=False)
            
            # --- Geminiでタグ生成 ---
            task_title = task.title
            generated_tags_str = generate_tags_with_gemini(task_title) # Geminiからタグ文字列を取得
            
            # 生成されたタグ文字列を個別のタグ名に分割
            # 例: "#議事録 #難易度中" -> ["議事録", "難易度中"]
            tag_names = [name.strip().lstrip('#') for name in generated_tags_str.split() if name.strip().startswith('#')]
            
            task.save() # Taskインスタンスを先に保存してpkを確定させる (ManyToManyのため)

            # --- Tagモデルとの連携 ---
            for tag_name in tag_names:
                # 既存のタグがあれば取得、なければ新規作成
                tag, created = Tag.objects.get_or_create(name=tag_name)
                task.tags.add(tag) # タスクにタグを追加 (ManyToManyFieldの操作)

            # デフォルトで「未着手」を設定 (Modelでdefault='unstarted'済みなので不要かもしれないが明示的に)
            task.status = 'unstarted' 
            # assigned_users はblank=Trueなので、登録時は空のまま

            task.save() # 最終的な変更を保存

            messages.success(request, 'タスクの登録が完了しました！') # 成功メッセージ
            return redirect('task_register_page') # 登録後、同じページにリダイレクトしてフォームをクリア

        else:
            # バリデーションエラーがある場合
            # form.errors が自動的にテンプレートに渡される
            messages.error(request, '入力内容にエラーがあります。ご確認ください。') # エラーメッセージ

    else:
        # GETリクエストの場合、空のフォームを表示
        form = TaskRegisterForm()

    context = {
        'page_title': 'タスク登録',
        'form': form,
    }
    return render(request, 'tasks/task_register.html', context)

# --- 既存のビュー関数は省略 ---