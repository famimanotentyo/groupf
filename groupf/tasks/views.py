# groupf/tasks/views.py
from django.shortcuts import render

def top_page(request):
    """
    トップページを表示するビュー
    """
    # 将来的にここでデータベースからタスク情報を取得し、context経由でテンプレートに渡します。
    context = {}
    return render(request, 'tasks/index.html', context)
