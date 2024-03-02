from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('reg', views.reg, name='register'),
    path('login', views.login_user, name='login'),
    path('profile', views.profile, name='profile'),
    path('profile/<int:product_id>', views.show_open, name='show_open'),
]
