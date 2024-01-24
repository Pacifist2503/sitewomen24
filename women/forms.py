from django import forms
from .models import Category, Husband


class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255, label='Заголовок')
    slug = forms.SlugField(max_length=255, label='URL')
    content = forms.CharField(widget=forms.Textarea(), required=False, label='Описание')
    is_published = forms.BooleanField(required=False, label='Статус')
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория', empty_label='Не выбрано')
    husband = forms.ModelChoiceField(queryset=Husband.objects.all(), required=False, label='Муж', empty_label='Не выбрано')
