from django import forms
from .models import News

class NewsCreateForm(forms.ModelForm):
    class Meta:
        model = News
        # 使用するフィールド
        fields = ('title', 'link')
