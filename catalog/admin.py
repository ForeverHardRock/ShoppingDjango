from django.contrib import admin
from .models import Category, SubCategory, Product
from .forms import CategoryForm, SubCategoryForm, ProductForm
from django.utils.html import format_html


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    form = CategoryForm
    list_display = ['category',]
    ordering = ['category']
    list_per_page = 20


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    form = SubCategoryForm
    list_display = ['subcategory', 'sub_category_id']
    list_editable = ['sub_category_id']
    ordering = ['sub_category']
    list_per_page = 20


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductForm
    list_display = ['product', 'prod_subcategory_id', 'price', 'image_preview']
    list_editable = ['prod_subcategory_id', 'price']
    ordering = ['product']
    search_field = ['product']
    list_per_page = 20

    def image_preview(self, obj):
        if obj.image:
            return format_html(f'<img src="{obj.image.url}" style="max-width: 100px; max-height: 100px;">')
        else:
            return 'No image'

    image_preview.short_description = 'Обложка'

