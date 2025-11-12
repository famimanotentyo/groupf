from django import forms
from .models import Task, Tag # TaskモデルとTagモデルをインポート

class TaskRegisterForm(forms.ModelForm):
    # due_date フィールドを DateTimeInput ウィジェットでオーバーライド
    # HTML5のdatetime-local形式を使うことで、ブラウザ標準の日時ピッカーを期待する
    due_date = forms.DateTimeField(
        label="期限",
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        input_formats=['%Y-%m-%dT%H:%M'], # HTML5のdatetime-local形式に対応
        help_text="タスクの完了期限を入力してください。カレンダーと時計アイコンから選択できます。"
    )

    class Meta:
        model = Task
        fields = ['title', 'due_date', 'notes'] # フォームで入力させるフィールドを指定

        labels = {
            'title': 'タスク名',
            'notes': 'タスク備考欄',
        }
        
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': '例: 議事録の作成', 'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'rows': 4, 'placeholder': 'タスクの詳細や補足事項を入力してください', 'class': 'form-control'}),
            # due_date は上でオーバーライドしているのでここには記述しない
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title:
            raise forms.ValidationError("タスク名は必須です。")
        if len(title) < 3:
            raise forms.ValidationError("タスク名は3文字以上で入力してください。")
        return title

    def clean_due_date(self):
        due_date = self.cleaned_data.get('due_date')
        if not due_date:
            raise forms.ValidationError("期限は必須です。")
        # 例: 過去の日付を設定できないようにするバリデーション
        # if due_date < timezone.now():
        #     raise forms.ValidationError("期限は未来の日付を設定してください。")
        return due_date