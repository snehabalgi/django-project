from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
  path ('', views.home, name='home'),
  path('add/', views.add_coffee, name='add_coffee'),
  path('add_to_cart/<int:coffee_id>/', views.add_to_cart, name='add_to_cart'),
  path('cart/', views.cart, name='cart'),
  path('clear_cart/', views.clear_cart, name='clear_cart'),
    path('update_cart/<int:cart_id>/', views.update_cart, name='update_cart'),
    path('remove_from_cart/<int:cart_id>/', views.remove_from_cart, name='remove_from_cart'),
  path('about/', views.about, name='about'),
  path('coffee/<int:coffee_id>/', views.coffee_detail, name='coffee_detail'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)