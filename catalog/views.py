from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

# Create your views here.
 
def home(request):
    carusel = Carusel_up_to_five_images.objects.all()
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()
    news = New.objects.all()
    return render(request, 'home.html', {
        'carusel': carusel,
        'categories': categories,
        'subcategories': subcategories,
        'news': news,
    })


def products(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()
    category = request.GET.get('category')
    company = request.GET.get('company')
    search = request.GET.get('search', '')
    subcategory = request.GET.get('subcategory')

    if subcategory:
        # subcategories = subcategories.filter(category=subcategory.category)
        products = products.filter(subcategory=subcategory)
    if category:
        products = products.filter(category=category)
    if company:
        products = products.filter(company=company)

    if search:
        search_results = products.filter(
            Q(name__icontains=search) |
            Q(category__name__icontains=search) |
            Q(company__name__icontains=search)
        )
        # If there are no search results, keep the original products queryset
        if not search_results.exists():
            search_results = products
        products = search_results

    return render(request, 'products.html', {
        'products': products,
        'categories': categories,
        'subcategories': subcategories,
    })


def map(request):
    return render(request, 'map.html')

def add_to_favorites(request, product_id):
    favorites = request.session.get('favorites', [])
    if product_id not in favorites:
        favorites.append(product_id)
        request.session['favorites'] = favorites
    # return redirect('catalog:products')
    return redirect(request.META.get('HTTP_REFERER', 'catalog:products'))
    # return HttpResponse("Added to favorites successfully")


def remove_from_favorites(request, product_id):
    favorites = request.session.get('favorites', [])
    if product_id in favorites:
        favorites.remove(product_id)
        request.session['favorites'] = favorites
    # return redirect('catalog:products')
    return redirect(request.META.get('HTTP_REFERER', 'catalog:products'))
    # return HttpResponse("Removed from favorites successfully")

def favorites_list(request):
    favorites = request.session.get('favorites', [])
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()
    products = Product.objects.filter(id__in=favorites)

    if products:
        return render(request, 'favorites_list.html', {
            'products': products,
            'categories': categories,
            'subcategories': subcategories,
            })
    messages.success(request, 'Нет избранных товаров !')
    return redirect('catalog:home')


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    products = Product.objects.all()
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()


    return render(request, 'product_detail.html', {
        'product': product,
        'products': products,
        'categories': categories,
        'subcategories': subcategories,
    })