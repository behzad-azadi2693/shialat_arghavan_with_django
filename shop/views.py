from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import ProductModel, CategoryModel, ProductsImagesModel
from django.shortcuts import get_object_or_404
from .forms import ContactForm
import folium
# Create your views here.


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['new_product'] = ProductModel.objects.filter(new_product=True, public=True)[:6]
        context['products'] = ProductModel.objects.filter(new_product=False, public=True)[:6]

        return context


class DetailProductView(DetailView):
    slug_field = 'slug'	
    slug_url_kwarg = 'slug'	
    template_name = 'product.html'
    context_object_name = 'product'

    def get_object(self, queryset=None):
        obj = get_object_or_404(ProductModel, public=True, slug=self.kwargs.get(self.slug_url_kwarg))
        return obj


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = ProductsImagesModel.objects.filter(product__slug=self.kwargs.get(self.slug_url_kwarg))
        context['categories'] = ProductModel.objects.filter(category=self.get_object().category).exclude(slug=self.kwargs.get(self.slug_url_kwarg))
        return context

class ProductListView(ListView):
    template_name = 'products.html'
    queryset = ProductModel.objects.filter(public=True)
    context_object_name = 'products'


class ProductNewListView(ListView):
    template_name = 'products.html'
    queryset = ProductModel.objects.filter(public=True, new_product=True)
    context_object_name = 'products'


class ShopView(TemplateView):
    template_name = 'shop.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = ProductModel.objects.all()[:4]

        map = folium.Map([36.392475, 59.510601], zoom_start=13)
        folium.Marker(
            [36.392475, 59.510601], 
            popup=f'شیرآلات ارغوان',
            icon=folium.Icon(color='red')
        ).add_to(map)

        context['map'] = map._repr_html_()

        return context


class CategoryListView(ListView):
    template_name = 'category.html'
    model = CategoryModel
    context_object_name = 'categories'


class CategoryView(ListView):
    template_name = 'products.html'
    context_object_name = 'products'

    def get_queryset(self):
        products = ProductModel.objects.filter(category__name=self.kwargs.get('slug'))
        return products


class ContactView(CreateView):
    template_name = 'contact.html'
    form_class = ContactForm
    context_object_name = 'form'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        map = folium.Map([36.392475, 59.510601], zoom_start=13)
        folium.Marker(
            [36.392475, 59.510601], 
            popup=f'شیرآلات ارغوان',
            icon=folium.Icon(color='red')
        ).add_to(map)

        context['map'] = map._repr_html_()

        return context

class SearchView(TemplateView):
    template_name = 'products.html'
    queryset = ProductModel.objects.filter(public=True)
    context_object_name = 'products'


class SearchView(ListView):
    model = ProductModel
    template_name = 'search.html'
    context_object_name = 'products'

    def get_queryset(self, *args, **kwargs):
        products = self.model.objects.all()
        search = self.request.GET.get('q', '')
        if search:
            products = ProductModel.objects.filter(search__icontains = search)
        
        return products