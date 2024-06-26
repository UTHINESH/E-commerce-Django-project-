from django.urls import path, include
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    # path('login',views.login_page,name='login'),
    path('', include('django.contrib.auth.urls')),
    path('collections',views.collections,name='collection'),
    path('collections/<str:name>',views.collectionsview,name='collections'),
    path('collections/<str:cname>/<str:pname>',views.product_details,name='product_details'),
    path('search/', views.search, name='search'),
    path('addtocart', views.add_to_cart, name='addtocart'),
    path('cart', views.cart_page, name='cart'),
    path('fav', views.fav_page, name='fav'),
    path('favviewpage',views.favviewpage,name="favviewpage"),
    path('remove_fav/<str:fid>',views.remove_fav,name="remove_fav"),
    path('remove_cart/<str:cid>', views.remove_cart, name='remove_cart'),
]