from django.core.exceptions import ValidationError
from django.db import models
from slugify import slugify
from django_ckeditor_5.fields import CKEditor5Field


class Category(models.Model):
    category = models.CharField(max_length=100, verbose_name='Категория')
    category_en = models.CharField(max_length=100, blank=False)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def save(self, *args, **kwargs):
        if self.category:
            self.category_en = slugify(self.category)
        super(Category, self).save(*args, **kwargs)


class SubCategory(models.Model):
    subcategory = models.CharField(max_length=100, verbose_name='Подкатегория')
    subcategory_en = models.CharField(max_length=100, blank=False)
    sub_category_id = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories', verbose_name='Категория')
    sub_category = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.subcategory

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    def save(self, *args, **kwargs):

        self.sub_category = str(self.sub_category_id)
        self.subcategory_en = slugify(self.subcategory)

        super(SubCategory, self).save(*args, **kwargs)


class Product(models.Model):
    product_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    product = models.CharField(max_length=100, verbose_name='Наименование')
    product_en = models.CharField(max_length=100, blank=False)
    image = models.ImageField(upload_to='product_images/', verbose_name='Изображение')
    description = CKEditor5Field('Text', config_name='extends')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Стоимость')
    prod_category_id = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products',
                                            verbose_name='Категория')
    prod_subcategory_id = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='products', verbose_name='Подкатегория')
    prod_category = models.CharField(max_length=100)
    prod_subcategory = models.CharField(max_length=100)

    def __str__(self):
        return self.product

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def clean(self):
        if Product.objects.filter(product=self.product).exists() and self.product_id is None:
            raise ValidationError("Такой продукт уже существует")

    def save(self, *args, **kwargs):
        self.product_en = slugify(self.product)
        self.prod_subcategory = str(self.prod_subcategory_id)
        self.prod_category = str(self.prod_category_id)
        super(Product, self).save(*args, **kwargs)



