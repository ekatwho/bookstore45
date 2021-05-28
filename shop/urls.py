from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('shop/delivery/', views.delivery, name='delivery'),
    path('shop/about/', views.about, name='about'),
    path('shop/login/', views.login, name='login'),
    path('account/account/register/', views.register, name='register'),
    path('shop/register_done/', views.register_done, name='register_done'),

]

