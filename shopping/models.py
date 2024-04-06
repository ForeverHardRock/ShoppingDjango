from django.db import models


class Add_To_Cart(models.Model):
    potential_buyer = models.CharField(max_length=255, verbose_name='TG ID заказчика')
    items_in_cart = models.TextField(verbose_name='Товары')

    def __str__(self):
        return self.potential_buyer

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'


class Orders(models.Model):
    order_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    order_products = models.TextField(verbose_name='Товары')
    order_summ = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма заказа')
    order_time = models.DateTimeField(verbose_name='Время заказа')
    buyer_name = models.CharField(max_length=255, verbose_name='Имя заказчика')
    buyer_tg_id = models.CharField(max_length=255, verbose_name='TG ID заказчика')
    buyer_address = models.CharField(max_length=255, verbose_name='Адрес заказчика')

    def __str__(self):
        return self.order_products

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'