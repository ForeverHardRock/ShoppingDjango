from django.contrib import admin
from .models import FAQ
from .forms import FAQForm


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    form = FAQForm
    list_display = ['question', 'answer']
    ordering = ['answer']
    search_field = ['answer']
    list_per_page = 20
