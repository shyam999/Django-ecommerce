from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.shop_index, name='shop_index'),
    path('about/', views.about, name='about'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('product/', views.product_list, name='product_list'),
    path('product/<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('product/<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    #path for categories
    path('categories/',views.categories,name="categories"),
    

]