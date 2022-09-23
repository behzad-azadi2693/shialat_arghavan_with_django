from django.contrib import admin
from .models import ProductModel, ProductsImagesModel, ContactModel, CategoryModel


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image')

@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject')

class ProductsImagesModelAdmin(admin.TabularInline):
    model = ProductsImagesModel
    fields = ( 'image',)


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('id','name','price','public','new_product', 'image')
    inlines = [
        ProductsImagesModelAdmin,
    ]    