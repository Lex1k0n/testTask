from django.shortcuts import render, redirect
from .serializers import ProductSerializer
from .models import ProductModel, AccessModel, GroupModel, LessonModels, GroupMembers
from rest_framework import renderers
import json
import datetime
import pytz
from .forms import ProductForm, LessonForm
from django.contrib.auth.models import User


def products(request):
    user = request.user
    if request.method == 'POST':
        if 'get' in request.POST:
            return redirect('show_product')
        elif 'main' in request.POST:
            return redirect('main')
    product_query = ProductModel.objects.all()
    s_obj = ProductSerializer(instance=product_query, many=True)
    json_render = renderers.JSONRenderer()
    out_data = json.loads(json_render.render(data=s_obj.data))
    for d in out_data:
        d['count'] = len(AccessModel.objects.select_related('product').filter(product_id=d['id']))
        d['percentage'] = str(int((d['count'] / (d['group_count'] * d['max_part'])) * 100)) + '%'
        d['buy_percent'] = str(int((d['count'] / User.objects.all().count()) * 100)) + '%'
    return render(request, 'products/products.html', {'data': out_data, 'user': user})


def show_product(request, product_id):
    product = ProductModel.objects.get(id=product_id)
    user = request.user
    form = LessonForm()
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if 'back' in request.POST:
            return redirect('products')
        elif 'buy' in request.POST:
            if request.user.is_authenticated and len(AccessModel.objects.filter(product_id=product.pk,
                                                                                user_id=request.user)) == 0:
                groups = GroupModel.objects.filter(product_id=product_id)
                is_first_free_group = True
                have_free_group = False
                target_group = None
                target_count = product.max_part
                target_min_group = None
                target_min_count = -1
                free_users = 1
                free_group = None
                utc = pytz.UTC
                now_time = datetime.datetime.now().replace(tzinfo=utc)
                start_time = product.starttime.replace(tzinfo=utc)
                for group in groups:
                    length = len(GroupMembers.objects.select_related('user').filter(group_id=group.id))
                    if length < product.min_part:
                        have_free_group = True
                        if is_first_free_group:
                            GroupMembers.objects.create(user=user, group=group)
                            AccessModel.objects.create(user=request.user, product=product)
                            return redirect('products')
                        else:
                            if length > target_min_count:
                                target_min_group = group
                            if free_group is None:
                                free_group = group
                    elif length == product.max_part:
                        is_first_free_group = False
                        continue
                    else:
                        have_free_group = True
                        free_users += length - product.min_part
                        if length < target_count:
                            target_group = group
                            target_count = length
                    is_first_free_group = False
                if not have_free_group:
                    return redirect('full_group')
                elif free_users == product.min_part and free_group is not None and now_time < start_time:
                    for group in groups:
                        length = len(GroupMembers.objects.select_related('user').filter(group=group))
                        while length > product.min_part:
                            current_user = GroupMembers.objects.select_related('user').filter(group=group)[0]
                            current_user.group = free_group
                            current_user.save()
                            length -= 1
                    GroupMembers.objects.create(user=user, group=free_group)
                    AccessModel.objects.create(user=request.user, product=product)
                    return redirect('products')
                elif target_group is None and target_min_group is not None:
                    GroupMembers.objects.create(user=user, group=target_min_group)
                    AccessModel.objects.create(user=request.user, product=product)
                    return redirect('products')
                else:
                    GroupMembers.objects.create(user=user, group=target_group)
                    AccessModel.objects.create(user=request.user, product=product)
                    return redirect('products')
            elif request.user.is_authenticated:
                return redirect('profile')
            else:
                return redirect('login')
        elif 'add' in request.POST:
            if form.is_valid():
                data = form.cleaned_data
                LessonModels.objects.create(title=data['title'], ref=data['ref'], product=product)
                return redirect('product_show', product_id=product_id)
    return render(request, 'products/show_product.html', {'product': product, 'user': user, 'form': form})


def complete(request):
    if request.method == 'POST':
        if 'main' in request.POST:
            return redirect('main')
    return render(request, 'products/complete.html')


def create_product(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            new_product = form.save(commit=False)
            new_product.save()
            for i in range(new_product.group_count):
                GroupModel.objects.create(number=i+1, product=new_product)
            return redirect('products')
    user = request.user
    return render(request, 'products/create.html', {'form': form, 'user': user})


def product_full(request):
    return render(request, 'products/full.html')
