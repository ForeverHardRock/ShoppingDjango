from django import forms
from .models import Mailing
from django_ckeditor_5.widgets import CKEditor5Widget


class MailingForm(forms.ModelForm):
    class Meta:
        model = Mailing
        fields = ['mail_title', 'mail_text']
        labels = {
            'mail_title': 'Название товара',
            'mail_text': 'Изображение товара',
        }
        widgets = {
            "mail_text": CKEditor5Widget(
                attrs={"class": "django_ckeditor_5"},
            )
        }