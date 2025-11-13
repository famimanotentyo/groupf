from django.db import models
from django.contrib.auth.models import User # Djangoの標準ユーザーモデルをインポート

# Tagモデルの定義
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="タグ名")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "タグ"
        verbose_name_plural = "タグ"
        ordering = ['name'] # タグ名をアルファベット順で並び替える

class Task(models.Model):
    # タスク名 (文字列、必須)
    title = models.CharField(max_length=200, verbose_name="タスク名")
    
    # 完了予定日 (日付と時間、必須)
    due_date = models.DateTimeField(verbose_name="期限")
    
    # タグ (Tagモデルへの多対多リレーションシップ、空を許容)
    # Geminiが生成したタグは、ここで既存のTagと関連付けたり、新しいTagを作成して関連付ける
    tags = models.ManyToManyField(Tag, blank=True, related_name='tasks', verbose_name="タグ")
    
    # タスク状態 (選択肢形式、デフォルトは「未着手」)
    STATUS_CHOICES = [
        ('unstarted', '未着手'),
        ('in_progress', '取り掛かり中'),
        ('pending_review', '確認待ち'),
        ('completed', '完了'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='unstarted', verbose_name="タスク状態")
    
    # 取り掛かり中の人 (複数選択可能、登録時は空を許容)
    assigned_users = models.ManyToManyField(User, related_name='assigned_tasks', blank=True, verbose_name="取り掛かり中の人")
    
    # タスク備考欄 (テキスト、空を許容)
    notes = models.TextField(blank=True, verbose_name="タスク備考欄")

    # 作成日 (自動で現在日時が設定される)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日時")
    
    # 更新日 (更新時に自動で現在日時が設定される)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日時")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "タスク"
        verbose_name_plural = "タスク"
        # 期限が近いもの、状態（未着手→完了の順など）で並び替える
        ordering = ['due_date', 'status']