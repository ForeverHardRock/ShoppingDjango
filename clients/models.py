from django.db import models
import datetime


class Clients(models.Model):
    client_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    client_name = models.CharField(max_length=255, verbose_name='Имя клиента')
    client_tg_id = models.CharField(max_length=255, verbose_name='TG ID клиента')
    client_orders = models.TextField(verbose_name='Заказы клиента')
    client_addresses = models.TextField(verbose_name='Адреса клиента')
    client_time = models.DateTimeField(verbose_name='Дата вступления')

    def __str__(self):
        return self.client_name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Mailing(models.Model):
    mail_title = models.CharField(max_length=255, verbose_name='Тема рассылки')
    mail_text = models.TextField(verbose_name='Текст рассылки')
    mail_time = models.DateTimeField(verbose_name='Время отправки')

    def __str__(self):
        return self.mail_text

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'

    def save(self, *args, **kwargs):
        if not self.mail_time:
            self.mail_time = datetime.datetime.now().replace(microsecond=0)
        super().save(*args, **kwargs)
