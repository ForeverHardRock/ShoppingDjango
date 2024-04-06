from django.contrib import admin
from .models import Mailing, Clients
from .forms import MailingForm


@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ['client_id', 'client_name', 'client_tg_id']
    ordering = ['client_name']
    list_per_page = 20


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ['mail_title', 'mail_time']
    ordering = ['mail_time']
    list_per_page = 20