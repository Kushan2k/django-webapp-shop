from django.urls import path
from . import views


urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('about/', views.About, name='about'),
    path('product/', views.Products, name='products'),
    path('products/new-posted', views.NewItems, name='new-posted'),
    path('products/trending', views.Trending, name='trending'),
    path('item/<int:id>', views.Item, name='item'),

]
