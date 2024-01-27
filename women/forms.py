from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, MinLengthValidator, MaxLengthValidator
from django.utils.deconstruct import deconstructible

from .models import Category, Husband, Women


@deconstructible
class RussianValidator:
    ALLOWED_CHARS = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯабвгдеёжзийклмнопрстуфхцчшщбыъэюя0123456789- "
    code = 'russian'

    def __init__(self, message=None):
        self.message = message if message else 'Должны присутствовать только русские символы, дефис и пробел'

    def __call__(self, value, *args, **kwargs):
        if not (set(value) <= set(self.ALLOWED_CHARS)):
            raise ValidationError(self.message, code=self.code)


# class AddPostForm(forms.Form):
#     title = forms.CharField(max_length=255,
#                             min_length=5,
#                             label='Заголовок',
#                             widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Впиши'}),
#                             # validators=[RussianValidator()],
#                             error_messages={'required': 'Без заголовка - никак',
#                                             'min_length': 'Слишком короткий заголовок'})
#     slug = forms.SlugField(max_length=255,
#                            label='URL',
#                            validators=[MinLengthValidator(5, 'Минимум 5 символов'),
#                                        MaxLengthValidator(100, message='Максимум 5 символов')]
#                            )
#     content = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 5}), required=False, label='Описание')
#     is_published = forms.BooleanField(required=False, label='Статус', initial=True)
#     cat = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория', empty_label='Категория не выбрана')
#     husband = forms.ModelChoiceField(queryset=Husband.objects.all(), required=False, label='Муж',
#                                      empty_label='Не выбрано')
#
#     def clean_title(self):
#         title = self.cleaned_data['title']
#         ALLOWED_CHARS = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯабвгдеёжзийклмнопрстуфхцчшщбыъэюя0123456789- "
#         if not (set(title) <= set(ALLOWED_CHARS)):
#             raise ValidationError('Должны присутствовать только русские символы, дефис и пробел')
#         return title

class AddPostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Впиши'}),
                            error_messages={'required': 'Без заголовка - никак', 'min_length': 'Слишком короткий заголовок'},
                            label='Имя')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 5}), required=False, label='Описание')

    class Meta:
        model = Women
        fields = ['title', 'slug', 'content', 'photo', 'cat', 'tags', 'husband']

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 20:
            raise ValidationError('Слишком много символов')
        return title


class UploadFileForm(forms.Form):
    # file = forms.FileField(label='Файл')
    file = forms.ImageField(label='Файл')
