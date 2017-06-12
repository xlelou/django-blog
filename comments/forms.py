#encoding:utf-8
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment #表明该表单对应的数据库模型是Comment
        fields = ['content']
