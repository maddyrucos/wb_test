from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .forms import ProductSearchForm
from .models import Product
from .services.wb_parser import search_wb_products

def search_view(request):
    form = ProductSearchForm(request.GET or None)
    messages = []

    if request.method == "GET":
        products = []
        if form.is_valid() and form.cleaned_data.get("query"):
            params = {k: v for k, v in form.cleaned_data.items() if v is not None}
            products = search_wb_products(**params)
            for p in products:
                p['price_basic'] = p.get("priceU")
                p['price_total'] = p.get("salePriceU")
                p['rating'] = p.get("reviewRating", 0)
                p['price_basic_rub'] = p['price_basic'] / 100
                p['price_total_rub'] = p['price_total'] / 100
                p['nm_id'] = p.get('id')

            request.session['products'] = products
            messages.append(f'Товаров найдено: {len(products)}')

        return render(request, "wb_parser/search.html", {
            "form": form,
            "products": products,
            "messages": messages
        })

    elif request.method == "POST":
        products = request.session['products']
        if not products:
            return render(request, "wb_parser/search.html", {
                "form": form,
                "products": products
            })

        added=0
        for p in products:
            _, created = Product.objects.update_or_create(       
                nm_id = p['nm_id'],
                defaults={
                    'name': p['name'],
                    'price_basic': p['price_basic'],
                    'price_basic_rub': p['price_basic_rub'],
                    'price_total' : p['price_total'],
                    'price_total_rub': p['price_total_rub'],
                    'rating': p['rating'],
                    'feedbacks': p['feedbacks']
                }
            )
            if created:
                added += 1

        products = []
        messages.append(f"Добавлено {added} новых товаров.")
        return render(request, "wb_parser/search.html", {
            "form": form,
            "products": products,
            "messages": messages
        })

def dashboard(request):
    return render(request, "wb_parser/dashboard.html") 