from django.urls import path
from .views import (
        HomeView, DetailProductView, ContactView, 
        ShopView, ProductListView, ProductNewListView,
        CategoryView, CategoryListView, SearchView
    )

app_name = 'shop'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('product/list/', ProductListView.as_view(), name='product_list'),
    path('product/list/new/', ProductNewListView.as_view(), name='product_list_new'),
    path('product/<str:slug>/', DetailProductView.as_view(), name='product'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('category/list/', CategoryListView.as_view(), name='category_list'),
    path('category/<str:slug>/', CategoryView.as_view(), name='category'),
    path('search/', SearchView.as_view(), name='search'),
]