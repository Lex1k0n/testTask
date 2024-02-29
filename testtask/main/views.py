from django.shortcuts import render, redirect


def index(request):
    if request.method == 'POST':
        if 'products' in request.POST:
            return redirect('products')
    return render(request, 'main/index.html')


def products(request):
    if request.method == 'POST':
        if 'create' in request.POST:
            return redirect('create_product')
        elif 'show' in request.POST:
            return redirect('product_list')
    return render(request, 'main/products.html')
