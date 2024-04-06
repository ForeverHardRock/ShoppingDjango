from django import forms
from .models import Category, SubCategory, Product
from django_ckeditor_5.widgets import CKEditor5Widget

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category']
        labels = {
            'category': 'Название категории',
        }


class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = ['subcategory', 'sub_category_id']
        labels = {
            'subcategory': 'Название подкатегории',
            'sub_category_id': 'Категория',
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product', 'image', 'description', 'price', 'prod_category_id', 'prod_subcategory_id']
        labels = {
            'product': 'Название товара',
            'image': 'Изображение товара',
            'description': 'Описание товара',
            'price': 'Стоимость товара',
            'prod_category_id': 'Категория',
            'prod_subcategory_id': 'Подкатегория',
        }
        widgets = {
            "description": CKEditor5Widget(
                attrs={"class": "django_ckeditor_5"},
            )
        }




