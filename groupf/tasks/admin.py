# tasks/admin.py (例)
from django.contrib import admin
from .models import Task, Tag #,Project  Tagもインポート

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_assigned_users', 'get_tags', 'due_date', 'status', 'created_at')
    list_filter = ('status', 'tags', 'assigned_users')
    search_fields = ('title', 'notes', 'tags__name', 'assigned_users__username')
    date_hierarchy = 'created_at'

    # ManyToManyフィールドはlist_displayに直接指定できないため、メソッドで表示
    def get_assigned_users(self, obj):
        return ", ".join([user.username for user in obj.assigned_users.all()])
    get_assigned_users.short_description = '担当者'

    def get_tags(self, obj):
        return ", ".join([tag.name for tag in obj.tags.all()])
    get_tags.short_description = 'タグ'


@admin.register(Tag) # Tagモデルも登録
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# Projectモデルの登録 (もしあれば)
# @admin.register(Project)
# class ProjectAdmin(admin.ModelAdmin):
#     list_display = ('name', 'leader', 'created_at')
#     list_filter = ('leader',)
#     search_fields = ('name', 'description')