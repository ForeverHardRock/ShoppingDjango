from django import forms
from .models import FAQ
from django_ckeditor_5.widgets import CKEditor5Widget


class FAQForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = ['question', 'answer']
        labels = {
            'question': 'Вопрос',
            'answer': 'Ответ',
        }
        widgets = {
            "answer": CKEditor5Widget(
                attrs={"class": "django_ckeditor_5"},
            )
        }