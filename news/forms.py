from django import forms
from .models import News


class MylistNews(forms.ModelForm):
    class Meta:
        model = News
        # 使用するフィールド
        fields = ('title', 'link')
        # ordering = ['-created_on']
