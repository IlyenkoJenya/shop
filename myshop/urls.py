from django.urls import path
from . import views

app_name = 'myshop'

urlpatterns = [
    path('delivery/', views.delivery, name='delivery'),
    path('contact/', views.contact, name='contact'),
    path('', views.index, name='index'),
    path('fb/', views.fb, name='fb'),
    path('list/', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list,
         name='product_list_by_category'
         ),
    path('<int:id>/<slug:slug>', views.product_detail,
         name='product_detail'),
     
    path('delivery/', views.delivery, name='delivery'),
    path('contact/', views.contact, name='contact'),
    path('', views.index, name='index')
]
