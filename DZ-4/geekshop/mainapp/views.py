from django.shortcuts import render
from .models import Product, ProductCategory
from django.shortcuts import get_object_or_404
from basketapp.models import Basket
import random


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def get_hot_product():
    products = Product.objects.filter(is_active=True)
    return random.sample(list(products), 1)[0]


def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category). \
                        exclude(pk=hot_product.pk)[:3]

    return same_products


def main(request):
    prod_cat = ProductCategory.objects.all()
    return render(request, 'mainapp/index.html', context={'user': request.user, 'menu': {'main': 'Главная', 'catalogue': 'Каталог', 'contacts': 'Контакты'}, 'page': 'Главная', 'prod_cat': prod_cat})
    

def catalogue(request, pk=None):
    print(pk)
    prod_cat = ProductCategory.objects.all()
    basket = get_basket(request.user)
    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    if pk is not None:
        if pk == '0':
            products = Product.objects.all().order_by('price')
            prod_cat_all = {'name': 'Все'}
        else:
            prod_cat_all = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')

        return render(request, 'mainapp/catalogue/products_list.html', context={'user': request.user,
                                                                        'menu': {'main': 'Главная',
                                                                                 'catalogue': 'Каталог',
                                                                                 'contacts': 'Контакты'},
                                                                        'page': 'Каталог', 'products': products,
                                                                        'prod_cat_all': prod_cat_all, 'prod_cat': prod_cat})


    return render(request, 'mainapp/catalogue/index.html', context={'user': request.user,
                                                                    'menu': {'main': 'Главная',
                                                                             'catalogue': 'Каталог',
                                                                             'contacts': 'Контакты'},
                                                                    'page': 'Каталог',
                                                                    'products': same_products, 'prod_cat': prod_cat, 'hot_product': hot_product, 'same_products': same_products})


def contacts(request):
    prod_cat = ProductCategory.objects.all()
    return render(request, 'mainapp/contacts/index.html', context={'user': request.user, 'placeholder': {'name': 'ivan', 'email': 'mail@gmail.com', 'theme': 'покупка монитора'}, 'prod_cat': prod_cat, 'menu': {'main': 'Главная', 'catalogue': 'Каталог', 'contacts': 'Контакты'}, 'page': 'Контакты'})


def monitor(request):
    prod_cat = ProductCategory.objects.all()
    return render(request, r'mainapp/catalogue/monitor/Eizo ColorEdge CG318-4K/Samsung Galaxy S9 Plus 256GB.html', context={'user': request.user, 'menu': {'main': 'Главная', 'catalogue': 'Каталог', 'contacts': 'Контакты'}, 'prod_cat': prod_cat})
# Create your views here.


def product(request, pk):
    title = 'Продукт'
    prod_cat = ProductCategory.objects.all()
    context = {'title': title,
               'menu': {'main': 'Главная', 'catalogue': 'Каталог', 'contacts': 'Контакты'},
               'product': get_object_or_404(Product, pk=pk),
               'prod_cat': prod_cat
               }
    return render(request, 'mainapp/catalogue/product/product.html', context)

# Create your views here.
