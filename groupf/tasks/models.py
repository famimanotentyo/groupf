# tasks/models.py
from django.db import models
from django.contrib.auth.models import User # Django標準のユーザーモデル

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    # 「未着手」「着手中」「確認待ち」の状態
    STATUS_CHOICES = [
        ('todo', '未着手'),
        ('doing', '着手中'),
        ('done', '確認待ち'), # スケッチの「確認待ち」
    ]

    name = models.CharField(max_length=200, verbose_name="タスク名")
    deadline = models.DateTimeField(verbose_name="期限", null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='todo')
    
    # 「タスク割り当て」画面用
    # null=True, blank=True は「担当者未定」を許可する
    assignee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="担当者")
    
    # 「タグ生成」用（多対多の関係）
    tags = models.ManyToManyField(Tag, blank=True)
    
    # 「備考欄」用
    notes = models.TextField(verbose_name="備考欄", null=True, blank=True)

    def __str__(self):
        return self.name