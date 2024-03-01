from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from products.models import AccessModel, ProductModel, LessonModels
import datetime
import pytz


def index(request):
    if request.method == 'POST':
        if 'register' in request.POST:
            return redirect('register')
        elif 'login' in request.POST:
            return redirect('login')
        elif 'logout' in request.POST:
            logout(request)
            return redirect('main')
        elif 'profile' in request.POST:
            return redirect('profile')
        elif 'products' in request.POST:
            return redirect('products')
    return render(request, 'main/index.html', {'auth': request.user.is_authenticated})


def reg(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return redirect('main')
    return render(request, 'main/reg.html', {'form': form})


def login_user(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data['username'], password=data['password'])
            if user is not None:
                login(request, user)
                return redirect('main')

    return render(request, 'main/login.html', {'form': form})


def profile(request):
    user = request.user
    open_products = AccessModel.objects.select_related('product').filter(user_id=user.id)
    return render(request, 'main/profile.html', {'user': user, 'products': open_products})


def products(request):
    return render(request, 'main/products.html')


def show_open(request, product_id):
    utc = pytz.UTC
    product = ProductModel.objects.get(id=product_id)
    lessons = LessonModels.objects.select_related('product').filter(product_id=product_id)
    now_time = datetime.datetime.now().replace(tzinfo=utc)
    start_time = product.starttime.replace(tzinfo=utc)
    return render(request, 'main/show_open_product.html', {'product': product, 'is_started': now_time > start_time,
                                                           'lessons': lessons})
